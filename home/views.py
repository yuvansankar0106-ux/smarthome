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
def devices(request):
    return render(request, 'home/devices.html')
def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # yuvan / 1234 thaan correct da
        if username == 'yuvan' and password == '1234':
            return redirect('verify_otp')
        else:
            error = "Password thappu da macha! yuvan / 1234 adi"
    return render(request, 'login.html', {'error': error})