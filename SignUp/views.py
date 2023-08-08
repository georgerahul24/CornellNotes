from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from Home.views import Home
from django.contrib.auth.hashers import make_password, check_password


class SignUp(View):
    def get(self, request):
        form = SignUpForm()

        return render(request, 'SignUpPage.html', {'f': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data["name"], form.cleaned_data["email"],
                                            form.cleaned_data["password"])

            user.set_password(form.cleaned_data["password"])
            user.save()

            user = authenticate(request, username=form.cleaned_data["name"], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
            else:
                return HttpResponse("Error")

            print(form.cleaned_data["password"])
            return Home.as_view()(self.request)




        else:
            field_errors = [(field.label, field.errors) for field in form]
            return HttpResponse(f"Invalid Form {field_errors}")


class SignOut(View):
    def get(self, request):
        logout(request)
        return Home.as_view()(self.request)
