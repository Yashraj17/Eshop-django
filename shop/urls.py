from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import *
urlpatterns = [
    path("",homePage,name='homePage'),
    path("/filter/<slug>",filterCat,name='filter'),
    path('search/',search,name='search')
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)