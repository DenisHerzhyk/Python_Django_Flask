from django.shortcuts import render, redirect
from .models import Clients
from .forms import ClientsForm


def index(request):
    if request.method == 'POST':
        form = ClientsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('display')
    else:
        form = ClientsForm()
    context = {'form': form}
    return render(request, 'index.html', context)


def display(request):
    clients = Clients.objects.all()
    context = {'clients': clients}
    return render(request, 'display.html', context)
