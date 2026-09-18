from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        # demo login - yuvan / 1234
        return redirect('verify_otp')
    return render(request, 'login.html')

def verify_otp(request):
    if request.method == 'POST':
        return redirect('dashboard')
    return render(request, 'verify_otp.html')

def dashboard(request):
    return render(request, 'dashboard.html')

# ithu thaan missing ah irunthathu da - ithu fix pannidum
def security(request):
    return render(request, 'dashboard.html')

def devices(request):
    return render(request, 'dashboard.html')

def energy(request):
    return render(request, 'dashboard.html')

def automation(request):
    return render(request, 'dashboard.html')

def settings_view(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    return redirect('login')

# vere ethachum url miss aana ithu handle pannum
def settings(request):
    return render(request, 'dashboard.html')