from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
import sqlite3
from django.shortcuts import render
from .models import Book
from .models import Project
from .models import Employee
from .models import Cart
from .models import Employee, Project,Team , Product
from .forms import BookForm
from .forms import ClientForm
from .forms import ProjectForm
from .forms import EmployeeForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import TeamProjectForm
from django.utils import timezone
from django.utils.dateparse import parse_date
from .forms import CustomUserCreationForm


@login_required
def home(request):
    return render(request, "home.html")

def logout_now(request):
    return HttpResponse("<h1>Вы вышли из аккаунта</h1> Приходите еще!")


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def books_catalog(request):
    book = Book.objects.get
    return render(request, "book_form.html", {"book": book})
def books(request):
    books = Book.objects.all()  # все книги в queryset
    return render(request, "book_list.html", {"books": books})


def permission_denied(request, exception):
    return render(request, '403.html', status=403)
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "book_detail.html", {"book": book})


def project_detail(request, name_id):
    name = Project.objects.get(id=name_id)
    return render(request, "project_detail.html", {"name": name})


def employee_detail(request, name_id):
    name = Employee.objects.get(id=name_id)
    return render(request, "employee_detail.html", {"name": name})


def employee_list(request):
    query = request.GET.get('q')
    if query:
        employees = Employee.objects.filter(name__icontains=query)
    else:
        employees = Employee.objects.all()

    return render(request, 'employee_list.html', {'employees': employees})

def search_employees(request):
    query = request.GET.get('q', '')
    team_filter = request.GET.get('team', '')

    employees = Employee.objects.all()

    if query:
        employees = employees.filter(name__icontains=query)

    if team_filter:
        employees = employees.filter(team__id=team_filter)

    teams = Project.objects.all()

    # проверяйте названия файлов, так как в проекте ученика они могут отличаться

    return render(request, 'employee_list.html', {'employees': employees, 'teams': teams, 'selected_team': team_filter})

def book_create_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Автоматически сохраняет данные в базе данных
            print(Book.objects.all())
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправление на главную страницу после успешного создания клиента
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправление на главную страницу после успешного создания работника
    else:
        form = ProjectForm()
    return render(request, 'project_form.html', {'form': form})

#привязка мероприятия к команде
@login_required
def assign_team_project(request):
    if request.method == 'POST':
        form = TeamProjectForm(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            event = form.cleaned_data['event']
            team.event = event
            team.save()
            return redirect('home')  # Замени 'home' на свою целевую страницу
    else:
        form = TeamProjectForm()
    return render(request, 'assign_team_project.html', {'form': form})

#вывод всех мероприятий + поиск по дате и фильтр по дате
def project_list(request):
    # Получаем параметр даты из GET-запроса
    date_filter = request.GET.get('date')
    if date_filter:
        # Преобразуем дату из строки в объект DateTime
        date_filter = timezone.datetime.strptime(date_filter, '%Y-%m-%d').date()
        projects = Project.objects.filter(date=date_filter)  # Фильтруем проекты по дате
        #есть вариант попроще, тут как нравится/ обязательно проверь библиотеки для работы с датой и ее преобразованием. Их куча там)
        # date = parse_date(query_date)
        # events = Project.objects.filter(date=date)
    else:
        projects = Project.objects.all()  # Если даты нет, получаем все проекты
    # projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})




def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()  # Автоматически сохраняет данные в базе данных
            print(Employee.objects.all())
    else:

        form = EmployeeForm()
        # return render(request, 'employee_list.html', {'form': form})
    return render(request, 'employee_form.html', {'form': form})






def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'sign_up.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/sign.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Замените 'home' на нужную страницу
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/sign.html', {'form': form})


def cart(request):
    cart_items = Cart().objects.all()
    context = {'cart_items': cart_items}
    return render(request, 'cart.html', context)


def add_to_cart(request):
    cart_items = Cart().objects.all()
    context = {'cart_items': cart_items}
    return render(request, 'cart.html', context)
