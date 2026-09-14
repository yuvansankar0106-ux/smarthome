from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        if request.POST['username']=='student' and request.POST['password']=='1234':
            request.session['user']='student'
            return redirect('dashboard')
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def security(request):
    if request.method == 'POST':
        request.session['alert'] = request.POST.get('alert')
        request.session['camera'] = request.POST.get('camera')
        return render(request, 'security.html', {'msg':'Alert Saved!'})
    return render(request, 'security.html', {
        'alert': request.session.get('alert','No Intrusion'),
        'camera': request.session.get('camera','ON')
    })

def devices(request):
    if request.method == 'POST':
        request.session['light'] = request.POST.get('light')
        request.session['door'] = request.POST.get('door')
        return render(request, 'devices.html', {'msg':'Devices Saved!'})
    return render(request, 'devices.html', {
        'light': request.session.get('light','OFF'),
        'door': request.session.get('door','LOCKED')
    })