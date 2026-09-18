from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        if u == 'yuvan' and p == '1234':
            return redirect('verify_otp')
    return render(request, 'login.html')

def verify_otp(request):
    if request.method == 'POST':
        # OTP entha number adichaalum ok da
        return redirect('dashboard')
    return render(request, 'verify_otp.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def security(request):
    return render(request, 'dashboard.html')
def devices(request):
    return render(request, 'dashboard.html')
def energy(request):
    return render(request, 'dashboard.html')
def automation(request):
    return render(request, 'dashboard.html')
def settings(request):
    return render(request, 'dashboard.html')
def logout_view(request):
    return redirect('login')