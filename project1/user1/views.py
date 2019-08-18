from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import *
from django.contrib import messages
from .forms import ContactForm , LoginForm,EditForm
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    update_session_auth_hash,

)
from django.contrib.auth.decorators import login_required



def register(request):

        # processing the data after the user has entered the details in the form
        if request.method == 'POST':
            form = ContactForm(request.POST)
            first_name = form.data['first_name']
            last_name = form.data['last_name']
            username = form.data['username']
            mail = form.data['mail']
            address = form.data['address']
            password = form.data["password"]
            password2 = form.data["password_again"]
            password3 = make_password(password)
            # checking if the the two passwords are same.
            if password == password2:
                # Checking if the username already exists in the database
                if User.objects.filter(username=username).exists():
                    print("username taken")
                    return HttpResponse('username already exists')
                else:
                    # Creating a new user with given details
                    q = User(first_name=first_name, last_name=last_name, username=username, email=mail,
                                 address=address, password=password3)
                    q.save()
                    messages.success(request, 'user registered successfully.')
                    response = redirect('../login/')
                    return response
            else:
                return HttpResponse('passwords are not same')
        else:
            # Rendering the form in html initially
            form = ContactForm()
            return render(request, 'user1/register.html', {'form': form})

# To login a current user
def loginview(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = form.data['username']
        password = form.data["password"]
        # Authenticating the user by checking in the database
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, username + 'You are now logged in..!!!.' )
            response = redirect('../home/')
            return response
        else:
            messages.error(request, 'username or password are not correct.')
            return render(request, 'user1/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'user1/login.html', {'form': form})

# Viewing the details of all the users in the home page
@login_required
def homeview(request):
    data = User.objects.all()
    return render(request, 'user1/home.html', {'User': data})

# To edit the details of the current user
@login_required
def edit(request):
    if request.method == 'POST':
        # rendering the model form and changing details
        form = EditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User profile updated.')
            return redirect('../home/')

    else :
        form = EditForm(instance=request.user)
    return render(request, 'user1/edit.html', {'form': form})

# To logout an already logged in user
@login_required
def logoutview(request):
    logout(request)
    response = redirect('../login/')
    return response




