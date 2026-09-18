from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('verify/', views.verify_otp, name='verify_otp'),
    path('logout/', views.logout_view, name='logout'),
    path('security/', views.security, name='security'),
    path('devices/', views.devices, name='devices'),
    path('energy/', views.energy, name='energy'),
    path('automation/', views.automation, name='automation'),
    path('settings/', views.settings_page, name='settings'),
]