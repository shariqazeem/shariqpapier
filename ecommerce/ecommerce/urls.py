"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('collections/all', views.shopall, name='shopall'),
    path('collections/<str:category_name>/', views.category, name='category'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update_cart_item/<int:product_id>/', views.update_cart_item, name='update_cart_item'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('complete_order', views.complete_order, name='complete_order'),
    # path('paypal_payment', views.paypal_payment, name='paypal_payment'),
    # path('paypal_redirect', views.paypal_redirect, name='paypal_redirect'),
    # path('paypal/success', views.paypal_success, name='paypal_success'),
    # path('paypal/cancel', views.paypal_cancel, name='paypal_cancel'),
    path('rate_calculator/', views.rate_calculator, name='rate_calculator'),
    path('save_rates/', views.save_rates, name='save_rates'),




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
