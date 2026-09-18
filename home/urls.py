from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('dashboard/', views.dashboard, name='dashboard2'),
    path('security/', views.security, name='security'),
    path('devices/', views.devices, name='devices'),
    path('energy/', views.energy, name='energy'),
    path('automation/', views.automation, name='automation'),
    path('settings/', views.settings, name='settings'),
    path('logout/', views.logout_view, name='logout'),
]