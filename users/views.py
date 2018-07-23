from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from .forms import LoginForm
from .models import User

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = fprm.cleaned_data
            user = authenticate(email=cd['email'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Pomyślnie zalogowany')
                else:
                    return HttpResponse('Konto nieaktywne')
            else:
                return HttpResponse('Użytkownik nie istnieje')
        else:
            form = LoginForm()
        return render(request,
                      'users/login.html',
                      {'form':form})
