from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages 

# Create your views here.
def home(request):
    context = {'title':'Home'}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        context['test'] = request.POST
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged In")
        else:
            messages.warning(request, "There was an error, please try again!")
        return redirect('home')
    return render(request, 'crm/home.html', context)
