from django.contrib.auth import authenticate, forms, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View

from .models import Employee


class Index(LoginRequiredMixin, View):
    template = "core/index.html"
    login_url = reverse_lazy("login")

    def get(self, request):
        employees = Employee.objects.all()
        return render(request, self.template, {"employees": employees})


class Login(View):
    template = "core/login.html"

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template, {"form": form})

    def post(self, request):
        post = request.POST
        form = AuthenticationForm(post)
        username = post["username"]
        password = post["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, self.template, {"form": form})
