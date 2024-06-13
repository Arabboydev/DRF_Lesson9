from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from . import models
from . import forms
from django.views import View


class Register(View):
    def get(self, request):
        registration_form = forms.RegistrationForm()
        context = {
            'registration_form': registration_form
        }
        return render(request, 'users/register.html', context=context)

    def post(self, request):
        registration_form = forms.RegistrationForm(data=request.POST, files=request.FILES)
        if registration_form.is_valid():
            print(f"{request} is valid")
            registration_form.save()
            return redirect('login')
        else:
            context = {
                'registration_form': registration_form
            }
            print(f'user -{request}  invalid')
            return render(request, 'users/register.html', context=context)


class Login(View):
    def get(self, request):
        login_form = AuthenticationForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'users/login.html', context=context)

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            account = login_form.get_user()
            login(request, account)
            return redirect('ListProducts')

        else:
            context = {
                'login_form': login_form
            }
            return render(request, 'users/login.html', context=context)