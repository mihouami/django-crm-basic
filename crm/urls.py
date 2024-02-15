from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("logout/", logout_user, name='logout'),
    path("register/", register_user, name='register'),
    path("contact/<int:pk>/", contact_detail, name='contact'),
    path("delete_contact/<int:pk>", delete_contact, name='delete_contact'),
    path('add_contact/', add_contact, name='add_contact'),
    path('update_contact/<int:id>', update_contact, name='update_contact'),
    path("company/<int:pk>/", company_detail, name='company'),
    #path("delete_company/<int:pk>/", delete_company, name='delete_company'),
]