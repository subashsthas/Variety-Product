from django.urls import path
from .import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "main"

urlpatterns = [
    path('', views.index, name="index"),
    # path('/<int:pk>', views.addToCart, name=" addToCart"),
    path('register/', views.register, name="register"),
    path('info/', views.info, name="info"),
    path("products/<int:product_id>", views.productView, name="ProductView"),
    path("product/<int:pk>/", views.delete_product, name="delete_product"),
    path("add_to_cart/<int:atc>/", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.cart, name="cart"),
    path("crud/", views.crud, name="crud"),
    path('update/<int:pk>/', views.update_customer, name="update_customer"),
    path("account/", views.accounts, name="accounts"),
    path("product_list/", views.product_list, name="product_list"),
    path('login/', views.login_request, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
