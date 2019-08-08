"""social_notes_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from myapp import views
from myapp.models import MyNotes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signUp, name='sign_up'),
    path('check_login/', views.checkLogin, name='check_login'),
    path('add_a_note/', views.addNote, name='add__a_note'),
    path('save_notes/', views.saveNote, name='save_note'),
    path('show_all_notes/', views.showAllNotes, name='show_all_notes'),
    path('user_registration/', views.userResigration, name='user_registration'),
    path('add_a_user/', views.addUser, name='add_a_user'),
    path('logout/', views.logOut, name='logout'),
    path('update<int:id>/', views.update, name='update'),
    path('note<int:id>/', views.updatenow, name='updatenow'),
    path('delete<int:id>/', views.deletenow, name='deletenow'),
    path('search_user/', views.searchUser, name='search_user'),
    path('searchByName/', views.searchByName, name='searchByName'),
    path('searchByMobile/', views.searchByMobile, name='searchByMobile'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
