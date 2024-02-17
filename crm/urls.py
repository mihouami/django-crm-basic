from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("logout/", logout_user, name='logout'),
    path("register/", register_user, name='register'),
    path("contacts/", contacts, name='contacts'),
    path("contact/<int:pk>/", contact_detail, name='contact'),
    path("delete_contact/<int:pk>/", delete_contact, name='delete_contact'),
    path('add_contact/', add_contact, name='add_contact'),
    path('update_contact/<int:id>/', update_contact, name='update_contact'),
    path("compagnies/", compagnies, name='compagnies'),
    path("add_company/", add_company, name='add_company'),
    path("company/<int:pk>/", company_detail, name='company'),
    path("update_company/<int:pk>/", update_company, name='update_company'),
    path("company/<int:pk>/add_contact/", add_contact_from_company, name='add_contactfromcompany'),
    #path("delete_company/<int:pk>/", delete_company, name='delete_company'),
]