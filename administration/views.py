from django.shortcuts import render
from django.urls import include
from django.contrib.auth.forms import AuthenticationForm



def login(request):
	form = AuthenticationForm()
	return render(request, "registration/login.html", context={"form":form})

def logout(request):
    messages.info(request, "Logged out successfully!")
    return redirect("registration/login.html")