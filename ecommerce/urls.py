from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from store import views
urlpatterns=[
path("admin/",admin.site.urls),
path("",views.home,name="home"),
path("product/<int:pk>/",views.product_detail,name="product_detail"),
path("cart/",views.cart,name="cart"),
path("cart/add/<int:pk>/",views.add_to_cart,name="add_to_cart"),
path("cart/remove/<int:pk>/",views.remove_from_cart,name="remove_from_cart"),
path("checkout/",views.checkout,name="checkout"),
path("orders/",views.orders,name="orders"),
path("register/",views.register,name="register"),
path("login/",auth_views.LoginView.as_view(template_name="registration/login.html"),name="login"),
path("logout/",auth_views.LogoutView.as_view(),name="logout"),
]
