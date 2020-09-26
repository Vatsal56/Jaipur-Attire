from django.shortcuts import render, redirect, HttpResponse, reverse
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile

def signup(request):
    if request.method == 'POST':
        if request.POST.get('password1') == request.POST.get('password2'):   
            try:
                user = User.objects.get(username=request.POST.get('username'))
                return render(request, 'accounts/signup.html', {'error':'The username has already been taken.'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST.get('username'), password=request.POST.get('password1'), first_name=request.POST.get('firstname'), last_name=request.POST.get('lastname'), email=request.POST.get('email'))
                newprofile = Profile(user=user, address=request.POST.get('address'), number=request.POST.get('number'), city=request.POST.get('city'), state=request.POST.get('state'), zipcode=request.POST.get('zipcode'))
                newprofile.save()
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error1':'The passwords did not match.'})
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error':'Login Failed: Incorrect Username or Password'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')