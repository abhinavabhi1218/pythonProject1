from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from.forms import *
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']

            em = form.cleaned_data['email']
            pm = form.cleaned_data['password']
            reg = Registration(name=nm, email=em, password=pm)

            reg.save()
            return render(request, 'forms.html', {'form':form})
    else:
        form = RegistrationForm()
        return render(request, 'forms.html', {'form':form})


def data_form(request):
    data = Registration.objects.all()
    return render(request, 'data.html', {'data':data})