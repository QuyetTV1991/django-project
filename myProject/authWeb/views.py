from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'myWebsite/login.html')

def signup(request):
    return render(request, 'myWebsite/signup.html')

def logout(request):
    pass