from django.shortcuts import render
from django.views import View

class Index(View):
    template = 'core/index.html'

    def get(self, request):
        return render(request,self.template)