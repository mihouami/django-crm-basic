from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'title':'Home'}
    return render(request, 'crm/home.html', context)
