from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from .forms import UserRegisterForm, AddContactForm, CompanyForm, AddContactFromCompanyForm
from .models import Contact, Company, Previous
from django.db.models import Count


#USERS VIEW

#HOME AND LOGIN PAGE
def home(request):
    contacts = Contact.objects.all()
    compagnies = Company.objects.all()
    context = {'title':'Home', 'contacts':contacts, 'compagnies':compagnies}
    context['request.method'] = request.method
    context['request'] = request
    context['compagnies_per_city'] = Company.objects.values('city').annotate(company_count=Count('id'))
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        context['test'] = request.POST
        

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged In.")
        else:
            messages.warning(request, "There was an error, please try again!")
        return redirect('home')
    
    return render(request, 'crm/home.html', context)

#LOGOUT & REGISTER VIEWS
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged Out.")
    return redirect('home')

def register_user(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have been successfully registered.')
                return redirect('home')
            else:
                messages.warning(request, 'Something went wrong.')
    context = {
                'title':'Register',
                'form':form,          
    }
    return render(request, 'crm/register.html', context)

#CONTACTS VIEWS
def contacts(request):
    if request.user.is_authenticated:
        contacts = Contact.objects.all()
        return render(request, 'crm/contacts.html', {'contacts':contacts})
    else:
        messages.warning(request, 'You must be logged In.')
        return redirect('home')


def contact_detail(request, pk):
    if request.user.is_authenticated:
        page = request.META.get('HTTP_REFERER')
        if 'update_contact' not in str(page) and page != None:
            Previous.objects.create(previous=page)
        context = {'contact':Contact.objects.get(id=pk), 'previous':Previous.objects.last().previous, 'page':type(page)}
        return render(request, 'crm/contact.html', context)
    else:
        messages.warning(request, 'You must be logged In.')
        return redirect('home')
    

def delete_contact(request, pk):
    if request.user.is_authenticated:
        contact = get_object_or_404(Contact, id=pk)
        contact.delete()
        messages.success(request, 'Contact has been deleted')
    else:
        messages.warning(request, 'You must be logged In.')
    return redirect('contacts')


def add_contact(request):
    if request.user.is_authenticated:
        form = AddContactForm(request.POST or None)
        page = request.META.get('HTTP_REFERER')
        if 'add_contact' not in str(page) and page != None:
            Previous.objects.create(previous=page)
        context = {'form':form, 'previous':Previous.objects.last().previous}
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Contact added')
                previous_page = request.META.get('HTTP_REFERER')
                return redirect(previous_page)
        return render(request, 'crm/add_contact2.html', context)
    else:
        messages.success(request, 'You need to be logged in to access this page')
        return redirect('home')


def update_contact(request, id):
    if request.user.is_authenticated:
        contact = get_object_or_404(Contact, pk=id)
        form = AddContactForm(request.POST or None, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact', pk=id)
        return render(request, 'crm/update_contact.html', {'form':form})
    else:
        messages.success(request, 'You need to be logged in to access this page')
        return redirect('home')


#COMPANY VIEWS
def compagnies(request):
     if request.user.is_authenticated:
         compagnies = Company.objects.all()
         return render(request, 'crm/compagnies.html', {'compagnies':compagnies})
     else:
        messages.success(request, 'You need to be logged in to access this page')
        return redirect('home')
         

def company_detail(request, pk):
    if request.user.is_authenticated:
        company = get_object_or_404(Company, pk=pk)
        if request.method == 'POST':
            if 'delete' in request.POST:
                company.delete()
                messages.success(request, 'Company has been deleted')
                return redirect('home')
        return render(request,'crm/company.html', {'company':company})
    else:
        messages.success(request, 'You need to be logged in to access this page')
        return redirect('home')
    

def add_company(request):
    if request.user.is_authenticated:
        form = CompanyForm(request.POST or None)
        page = request.META.get('HTTP_REFERER')
        if 'add_company' not in str(page) and page != None:
            Previous.objects.create(previous=page)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Company added')
                previous_page = request.META.get('HTTP_REFERER')
                return redirect(previous_page)
        context = {'form':form, 'previous':Previous.objects.last().previous}
        return render(request, 'crm/add_update_company.html', context)
    else:
        messages.success(request, 'You need to be logged in to access this page')
        return redirect('home')
    
def update_company(request, pk):
    if request.user.is_authenticated:
        company = Company.objects.get(id=pk)
        form = CompanyForm(request.POST or None, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record updated')
            return redirect('company', pk=pk)
        return render(request, 'crm/add_update_company.html', {'form':form})
    else:
        messages.warning(request, 'You need to be logged in to access this page')
        return redirect('home')
    
def add_contact_from_company(request, pk):
    if request.user.is_authenticated:
        company = Company.objects.get(id=pk)
        form = AddContactFromCompanyForm(request.POST or None)
        page = request.META.get('HTTP_REFERER')
        if 'add_contact' not in str(page) and page != None:
            Previous.objects.create(previous=page)
        if request.method == 'POST':
            if form.is_valid():
                contact = form.save(commit=False)
                contact.company = company
                form.save()
                messages.success(request, 'Contact added')
                previous_page = request.META.get('HTTP_REFERER')
                return redirect(previous_page)
        context = {'form':form, 'company':company, 'previous':Previous.objects.last().previous}
        return render(request, 'crm/add_contact2.html', context)
    else:
        messages.success(request, 'You need to be logged in to access this page')
        return redirect('home')


    
"""
def delete_company(request, pk):
    if request.user.is_authenticated:
        company = get_object_or_404(Company, pk=pk)
        company.delete()
        messages.success(request, 'Company has been deleted')
        return redirect('home')
    else:
        messages.success(request, 'You need to be logged in to access this page')
        return redirect('home')
"""

        






