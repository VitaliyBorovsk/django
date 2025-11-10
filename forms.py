from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Book, Product
from .models import Client
from .models import Employee
from .models import Project, Team
from .models import CustomUser

class CustomBookForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.CharField(max_length=100)
    extra_info = forms.CharField()

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "guests", "budget", "description","date"]

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'pages', 'price']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'birth_date', 'phone_number', 'email', 'discount_percentage', 'city']

class TeamProjectForm(forms.Form):
    team = forms.ModelChoiceField(queryset=Team.objects.all(), label="Выберите команду")
    event = forms.ModelChoiceField(queryset=Project.objects.all(), label="Выберите мероприятие")




class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user', 'name', 'birth_date', 'phone_number', 'email', 'city', 'team', 'salary']


class CustomUserCreationForm:
    pass

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')



