from django import forms
from .models import *
from django.contrib.auth.models import User

class Form(forms.Form):
    name=forms.CharField(error_messages={'required':'Enter Your Name'})
    father_Name=forms.CharField(error_messages={'required':'Enter Your Father Name'})
    mother_Name=forms.CharField(error_messages={'required':'Enter Your Mother Name'})
    contact=forms.CharField(error_messages={'required':'Enter Your Contact'})
    address=forms.CharField(error_messages={'required':'Enter Your Address'})
    email=forms.EmailField(error_messages={'required':"Enter Your Email"})
    password=forms.CharField(widget=forms.PasswordInput,error_messages={'required':"Enter Your Password"})
