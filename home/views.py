from django.shortcuts import render, redirect
from django.http import JsonResponse

def login_view(request):
    return render(request, 'login.html')

def dashboard(request):
    if request.method == 'POST':
        return JsonResponse({"status":"ok"})
    return render(request, 'dashboard.html')

def verify_otp_view(request):
    return redirect('/')
def logout_view(request):
    return redirect('/login/')
def security(request):
    return render(request, 'dashboard.html')

def energy(request):
    return render(request, 'dashboard.html')

def automation(request):
    return render(request, 'dashboard.html')

def settings(request):
    return render(request, 'dashboard.html')