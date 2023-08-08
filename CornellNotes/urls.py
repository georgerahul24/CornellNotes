"""
URL configuration for CornellNotes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Home.views import Home
from SignUp.views import SignUp, SignOut
from Login.views import Login
from About.views import About
from Notes.views import Notes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Home.as_view()),
    path('', Home.as_view()),
    path('SignUp/', SignUp.as_view(), name='SignUp'),
    path('LogOut/', SignOut.as_view(), name="LogOut"),
    path('LogIn/', Login.as_view(), name="LogIn"),
    path('About/', About.as_view(), name="About"),
    path('Notes/', Notes.as_view(), name="Notes")

]
