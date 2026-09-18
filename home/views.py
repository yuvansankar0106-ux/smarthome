from django.shortcuts import render
def login_view(request):
    return render(request, 'login.html')
def dashboard(request):
    return render(request, 'dashboard.html')
def verify_otp(r): return render(r,'login.html')
def logout_view(r): return render(r,'login.html')
def security(r): return render(r,'dashboard.html')
def devices(r): return render(r,'dashboard.html')
def energy(r): return render(r,'dashboard.html')
def automation(r): return render(r,'dashboard.html')
def settings_page(r): return render(r,'dashboard.html')