from django.contrib import admin
from django.urls import path, include
from.import views

urlpatterns = [
    path('',views.home),
    path('home/',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('product/',views.product,name="product"),
    path('cart/',views.cart,name="cart"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
]
