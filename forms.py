from django import forms
from django.contrib.auth.models import User


class CustomerForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Enter Your Name')
    age = forms.IntegerField(min_value=18, label='Enter Your Age')
    check = forms.BooleanField(required=False, label='Do You Want To Join Us')
    category = forms.ChoiceField(choices=[('student', 'student'), ('teacher', 'teacher'), ('administrator', 'administrator')])
class CustomerComplainForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','body']
        name = forms.CharField(max_length=100, required=True, label='Enter Your Name')
        email = forms.EmailField(max_length=30, required=True, label='Enter Your Email')
        body = forms.CharField(max_length=100, required=True, label='Enter Your complaint')

class StudentComplainForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','id', 'body']
        name = forms.CharField(max_length=20)
        id = forms.IntegerField
        body = forms.CharField(max_length=100)




class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='Enter Your First Name', max_length=10)
    last_name = forms.CharField(label='Enter Your Last Name', max_length=10)
    email = forms.EmailField(label='Enter Your email address', max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['first_name', 'last_name', 'email', 'password']



