from django.db import models
import sqlite3
from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    pass



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    image = models.ImageField(upload_to='bookImages/', blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)  # поле с текстом
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='booksImage/', null=True, blank=True)
    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    discount_percentage = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# связываем работника с проектом
class Project(models.Model):
    name = models.CharField(max_length=255)
    guests = models.IntegerField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=255)
    event = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='teams')

    def __str__(self):
        return self.name
class Employee(models.Model):
    # user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='employee')
    # name = models.CharField(max_length=100)
    # project = models.ForeignKey(Project, on_delete=models.CASCADE)  # связь моделей ОДИН-КО-МНОГИМ (одна запись в одной таблице может иметь много записей в другой
    # birth_year = models.IntegerField()
    # email = models.EmailField()
    # position = models.CharField(max_length=100)
    # salary = models.DecimalField(max_digits=10, decimal_places=2)
    # team = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='members')
    # team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='employees')
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='employee')
    name = models.CharField(max_length=255)
    birth_date = models.DateField(default='2000-01-01')
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='employees')
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name


class Cart(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.Product.title} x {self.quantity})"




# очередь работы с мероприятими в shell
    # from MYAPP.models import CustomUser, Project, Team, Employee
#
# # Создание пользователя
# user = CustomUser.objects.create(username='john_doe', password='your_password')  # Передавай необходимые параметры
#
# # Создание проекта
# project = Project.objects.create(
#     name='Kira',
#     guests=10,
#     budget=1000.00,
#     description='Пример проекта',
#     date='2025-02-03'
# )
#
# # Создание команды
# team = Team.objects.create(name='Team Alpha', event=project)
#
# # Создание объекта Employee
# employee = Employee.objects.create(
#     user=user,  # Передаем экземпляр CustomUser
#     name='John Doe',
#     birth_date='1990-01-01',
#     phone_number='1234567890',
#     email='john.doe@example.com',
#     city='Some City',
#     team=team,  # Передаем экземпляр Team
#     salary=50000.00
# )

# from pythonProject5.models import Product
#
# p = Product(name="Тестовая книга", price=300)
# p.image = "bookImages/example.png"  # путь относительно MEDIA_ROOT
# p.save()
#
#


# # Получаем объект - сотрудника
# employee1 = Employee.objects.get(id=1)
#
# # Теперь можно получить имя команды
# team_name = employee.team.name
#
# # Бюджет команды
# team_budget = employee.team.budget
# Пример рабочий
# e1 = Employee(name = "Бог" , project=Project.objects.get(id = 1),birth_year=7, position ="Главный волшебник", salary = 3, team = Project.objects.get(id = 1))
# a = Client(name = "dadad", birth_date = "22.11", phone_number = "294884", email = "daada@mail.ru", discount_percentage = "это я еще не перевела", city = "Не Москва")
#user = User.objects.create_user(username='newuser', email='newuser@example.com', password='password123')


