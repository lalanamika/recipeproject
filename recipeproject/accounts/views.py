from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:  # check for username uniqueness
                User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Error: Username already taken.'})
            except User.DoesNotExist:
                # the user account is created here and added in the model
                # user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                # login as that user
                user = authenticate(request, username=request.POST['username'], password=request.POST['password1'])
                login(request, user)
                return render(request, 'accounts/signup.html')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Error: Passwords did not match.'})
    else:
        if request.method == 'GET':
            return render(request, 'accounts/signup.html')

def loginview(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            if 'next' in request.POST:
                return redirect(request.POST["next"])
            return render(request, 'accounts/login.html', {'error': "Login successful !"})
        else:
            # Return an 'invalid login' error message.
            return render(request, 'accounts/login.html', {'error': "Error: Username and password did not match."})
    else:
        if request.method == 'GET':
            return render(request, 'accounts/login.html')
