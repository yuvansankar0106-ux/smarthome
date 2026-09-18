from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        if request.POST.get('username') == 'yuvan' and request.POST.get('password') == '1234':
            request.session['is_login'] = True
            return redirect('verify_otp')
        else:
            return render(request, 'login.html', {'error': 'yuvan / 1234 mattum da!'})
    return render(request, 'login.html')

def verify_otp(request):
    if not request.session.get('is_login'):
        return redirect('login')
    return render(request, 'verify_otp.html')

def dashboard(request):
    if not request.session.get('is_login'):
        return redirect('login')
    return render(request, 'dashboard.html')

def logout_view(request):
    request.session.flush()
    return redirect('login')

# ithu ellam dashboard thaan kattum
def security(r): 
    if not r.session.get('is_login'): return redirect('login')
    return render(r,'dashboard.html')
def devices(r):
    if not r.session.get('is_login'): return redirect('login')
    return render(r,'dashboard.html')
def energy(r):
    if not r.session.get('is_login'): return redirect('login')
    return render(r,'dashboard.html')
def automation(r):
    if not r.session.get('is_login'): return redirect('login')
    return render(r,'dashboard.html')
def settings_page(r):
    if not r.session.get('is_login'): return redirect('login')
    return render(r,'dashboard.html')