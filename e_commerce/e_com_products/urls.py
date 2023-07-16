from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.ProductApi.as_view(), name='product_api'),
    path('status_update/', views.ProductStatusApi.as_view(), name='product_status_api'),
]