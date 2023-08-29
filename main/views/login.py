# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
import random

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from main.models import Professional

# Login View
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            
            # Check if the user has done the registration
            try:
                professional = Professional.objects.get(user=user)
                if professional.profession is None:
                    return redirect('request_community_entry')
            except Professional.DoesNotExist:
                pass
            
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

# ... rest of your code ...

def user_logout(request):
    logout(request)
    return redirect('home')  # Redirect to the desired page after logout
