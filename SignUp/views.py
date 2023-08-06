from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class SignUp(View):
    def get(self, request):
        form = SignUpForm()

        return render(request, 'SignUpPage.html', {'f': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            User.objects.create_user(form.cleaned_data["name"], form.cleaned_data["email"],
                                     form.cleaned_data["password"])

            user = authenticate(request, username=form.cleaned_data["name"], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
            else:
                return HttpResponse("Error")

            return HttpResponse(
                f'{form.cleaned_data["name"]}, {form.cleaned_data["email"]}, {form.cleaned_data["password"]}')





        else:

            field_errors = [(field.label, field.errors) for field in form]
            return HttpResponse(f"Invalid Form {field_errors}")
