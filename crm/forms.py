from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailField, CharField, TextInput, ModelForm, ModelChoiceField, Select
from .models import Contact, Company


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'city')


class AddContactFromCompanyForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ['company']


class AddContactForm(ModelForm):
    first_name = CharField(label='', widget=TextInput(attrs={'class':'form-control', 'placeholder':'test'}))
    company = ModelChoiceField(
        queryset=Company.objects.all(), 
        label='', 
        widget=Select(attrs={'class':'form-control'})
    )
    """
    last_name = CharField(label='', widget=TextInput(attrs={'class':'form-control'}))
    email = CharField(label='', widget=TextInput(attrs={'class':'form-control'}))
    mobile = CharField(label='', widget=TextInput(attrs={'class':'form-control'}))
    position = CharField(label='', widget=TextInput(attrs={'class':'form-control'}))
    """
    class Meta:
        model = Contact
        fields = '__all__'


class UserRegisterForm(UserCreationForm):
    email = EmailField(label='Email', widget=TextInput(attrs={'placeholder':'Email'}))
    first_name = CharField(label='First Name', widget=TextInput(attrs={'placeholder':'First Name'}))
    last_name = CharField(label='Last Name', widget=TextInput(attrs={'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        #self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = 'Username'
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>30 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        self.fields['username'].max_length = 30
        
        #self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = 'Password'
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><small><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></small></ul>'
        
        #self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = 'Confirm Password'
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'