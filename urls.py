"""
URL configuration for pythonProject5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.conf.urls.static import static
from . import views, settings
from django.conf import settings
from django.contrib.auth.views import LogoutView, LoginView
# from django.urls import handler403
from .views import create_project
from .views import assign_team_project
from django.views.generic import TemplateView
from .views import project_list
from .views import  user_logout , user_login

from django.contrib import admin
from django.urls import path

handler403 = 'pythonProject5.views.permission_denied'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),

    # path('books/', views.book_list, name='book_list'),
    path("books/", views.books, name="books"),
    path("book/<int:book_id>", views.book_detail, name="book_detail"),
    path("project/<int:name_id>", views.project_detail, name="project_detail"),
    path("employee/<int:name_id>", views.employee_detail, name="employee_detail"),
    path('employees/', views.employee_list, name='employee_list'),
    path('custom_book_create/',views.book_create_view, name = 'book_create'),
    path('create_client/', views.create_client, name='create_client'),
    path('create_employee/', views.create_employee, name='create_employee'),

    path('accounts/login/', LoginView.as_view(), name = "login"),
    path('accounts/logout/', LogoutView.as_view(next_page="logout_now"), name = "logout"),
    path('logout_now', views.logout_now, name="logout_now"),
    path ('create_project/', views.create_project, name="create_project"),

    path('products/', views.product_list, name='product_list'),

    path('assign-team-project/', views.assign_team_project, name='assign_team_project'),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('project_list/', views.project_list, name='project_list'),

    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path("cart/<int:product_id>/", views.cart, name ="cart")

] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)