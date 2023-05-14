from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from users.forms import UserLoginForm, UserRegisterForm


# Create your views here.
class UserLoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'index.html')
        return render(request, 'login.html', {'form': form})


class UserRegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html')
        return render(request, 'register.html', {'form': form})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return render(request, 'index.html')
