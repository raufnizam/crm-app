from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Record

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Confirm Password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Firstname', 'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Lastname', 'class': 'form-control'}))
    email = forms.CharField(max_length=100, required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'email', 'class': 'form-control'}))
    phone = forms.CharField(max_length=100, required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'phone', 'class': 'form-control'}))
    address = forms.CharField(max_length=100, required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'address', 'class': 'form-control'}))
    city = forms.CharField(max_length=100, required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'city', 'class': 'form-control'}))
    state = forms.CharField(max_length=100, required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'state', 'class': 'form-control'}))
    zip_code = forms.CharField(max_length=100, required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'zipCode', 'class': 'form-control'}))

    class Meta:
        model = Record
        exclude = ("user",)
