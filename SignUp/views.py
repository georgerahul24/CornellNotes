from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.template import loader
from .forms import SignUpForm


class SignUp(View):
    def get(self, request):
        form = SignUpForm()

        return render(request, 'SignUpPage.html', {'f': form})

    def post(self, request):
        pass
