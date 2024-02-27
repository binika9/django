from django.db import models


# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return self.name


class Registration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=8)
    def __str__(self):
        return self.first_name


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['first_name', 'last_name', 'email', 'password']

