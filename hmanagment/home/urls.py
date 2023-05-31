from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', views.login, name='login'),

    path('', views.home, name='home'),

    path('booking/', views.booking, name='booking'),

    path('contact/', views.contact_view, name='contact'),

    path('department/', views.department, name='department'),

    path('doctors/', views.doctors, name='doctors'),
]
