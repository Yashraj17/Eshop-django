from django.shortcuts import render,redirect,get_object_or_404
from shop.models import *
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegisterForm
from .forms import AddressForm

# Create your views here.

def getCategory():
    return Category.objects.all()

def homePage(req):
    data ={}
    data['products']= Product.objects.all()
    data['category'] = getCategory()
    return render(req,'home.html',data)

def filterCat(req,slug):
    data ={}
    data['products']= Product.objects.filter(category__slug = slug)
    data['category'] = getCategory()
    return render(req,'home.html',data)

def search(req):
    search = req.GET.get('search')
    data ={}
    data['products']= Product.objects.filter(name__contains = search)
    data['category'] = getCategory()
    return render(req,'home.html',data)

def singleView(req,slug):
    data = {}
    data['category'] = getCategory()
    data['product'] = Product.objects.get(slug = slug)
    data['products'] = Product.objects.exclude(slug = slug)
    return render(req,'singleView.html',data)

def loginRequest(req):
    form = AuthenticationForm(req,data = req.POST)
    if req.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username,password = password)
            if user is not None:
                login(req,user)
                return redirect(homePage)
            else:
                messages.error(req,"Invalid username or password.")
                return render(req,'login.html')
    return render(req,'login.html',context={"form":form})

def logoutRequest(req):
    logout(req)
    return redirect(loginRequest)

def registrationRequest(req):
    form = RegisterForm(req.POST or None)
    if req.method == 'POST':
        if form.is_valid():
            form.save()
            # print("hello this is form data" + user)
            return redirect(loginRequest)
    return render(req,'register.html',context={"form":form})

def addToCart(req,slug):
    product = get_object_or_404(Product,slug=slug)
    order_item , created = OrderItem.objects.get_or_create(user=req.user,ordered=False,item=product)
    order_qs = Order.objects.filter(user = req.user , ordered = False)
    if order_qs.exists():
        order = order_qs[0]
        if(order.items.filter(item__slug = slug).exists()):
            order_item.qty += 1
            order_item.save()
        else:
            order.items.add(order_item)
        return redirect(cartPage)
    else:
        order = Order.objects.create(user = req.user)
        order.items.add(order_item)
        return redirect(cartPage)
def removeFromCart(req,slug):
    product = get_object_or_404(Product,slug = slug)
    order = Order.objects.get(user = req.user ,ordered = False)
    order_item = OrderItem.objects.get(user = req.user,ordered = False,item = product)
    if order:
        if(order.items.filter(item__slug = slug).exists()):
            if order_item.qty <=1:
                order_item.delete()
            else:
                order_item.qty -=1
                order_item.save()
        return redirect(cartPage)
def deleteFromCart(req,slug):
    product = get_object_or_404(Product,slug=slug)
    order = Order.objects.get(user = req.user ,ordered = False)
    order_item = OrderItem.objects.get(user = req.user,ordered = False,item = product)
    if order:
        if(order.items.filter(item__slug = slug).exists()):
            order_item.delete()
        return redirect(cartPage)
    
    
def cartPage(req):
    data = {}
    data['order'] = Order.objects.get(user= req.user,ordered =False)
    return render(req,'myCart.html',data)

def addCoupon(req):
    order = Order.objects.get(user = req.user,ordered = False)
    if req.method == 'POST':
        code = req.POST.get('code')
        if (Coupon.objects.filter(code =code).exists()):
            coupon = Coupon.objects.get(code =code)
            order.coupon = coupon 
            order.save()
            return redirect(cartPage)
        else:
            return redirect(cartPage)
        
def removeCoupon(req):
    order = Order.objects.get(user = req.user,ordered = False)
    order.coupon = None
    order.save()
    return redirect(cartPage)

def Checkout(req):
    form = AddressForm(req.POST or None)
    return render(req,'checkout.html',context={"form":form})