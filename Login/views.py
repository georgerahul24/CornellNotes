from django.shortcuts import render
from django.views import View
from Home.views import Home
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import LogInForm
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.

class Login(View):
    def get(self, request):

        if request.user.is_authenticated:
            return Home.as_view()(self.request)
        else:
            return render(request, 'LoginPage.html')

    def post(self, request):

        form = LogInForm(request.POST)
        if form.is_valid():

            user = authenticate(request, username=form.cleaned_data["name"],
                                password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return Home.as_view()(self.request)
            else:
                return Home.as_view()(self.request)

        return HttpResponse("Form not valid")
