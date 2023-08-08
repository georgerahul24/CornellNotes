from django.shortcuts import render
from django.views import View
from Home.views import Home


# Create your views here.
class Notes(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'NotesPage.html')

        return Home.as_view()(self.request)
