from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.template import loader


class Profile:
    name = "LOGIN"


class Home(View):
    def get(self, request):
        profile = Profile()


        template = loader.get_template('MainPage.html')
        context = {
            'profile': profile,
        }
        return HttpResponse(template.render(context, request))
