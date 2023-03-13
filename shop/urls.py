from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import *
urlpatterns = [
    path("",homePage,name='homePage'),
    path("filter/<slug>",filterCat,name='filter'),
    path('search/',search,name='search'),
    path('single-view/<slug>',singleView,name='singleview'),
    path('login/',loginRequest,name='loginPage'),
    path('logout/',logoutRequest,name='logout'),
    path('register/',registrationRequest,name='registerPage'),
    path('add-to-cart/<slug>',addToCart,name='addToCart'),
    path('remove-to-cart/<slug>',removeFromCart,name='removeToCart'),
    path('delete-to-cart/<slug>',deleteFromCart,name='deleteFromCart'),
    path('mycart/',cartPage,name='cartPage'),
    path('addCoupon/',addCoupon,name='addCoupon'),
    path('removeCoupon/',removeCoupon,name='removeCoupon'),
    path('checkout/',Checkout,name='checkout'),

]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)