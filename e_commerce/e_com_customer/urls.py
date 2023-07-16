from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.CustomerApi.as_view(), name='customer_api'),
]