from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm


def signup(request):
    if request.method == "POST":
        forms = UserForm(request.POST)
        if forms.is_valid():
            forms.save()
            username = forms.cleaned_data.get('username')
            raw_password = forms.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        forms = UserForm()
    return render(request, 'common/signup.html', {'form': forms})
