"""diplom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.http import HttpResponseRedirect
from .views import ArticleView, CategoryView, ProductView, cart, register


urlpatterns = [
    path('', lambda x: HttpResponseRedirect('/shop/')),
    path('shop/', ArticleView.as_view(), name='articles'),
    path('shop/category/<slug:slug>/', CategoryView.as_view(), name='category'),
    path('shop/product/<slug:slug>/', ProductView.as_view(), name='product'),
    path('shop/cart/', cart, name='cart'),
    path('accounts/register/', register, name='register'),
]
