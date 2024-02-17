from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TasksForm
from django.utils import timezone


def index(request):
    if request.method == "POST":
        form = TasksForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            if task.completed:
                task.completed_at = timezone.now()
            task.save()
        return redirect('display')
    else:
        form = TasksForm()
    context = {'form': form}
    return render(request, 'index.html', context)


def display(request):
    completed_tasks = Tasks.objects.filter(completed_at__isnull=False)
    context = {'completed_tasks': completed_tasks}
    return render(request, 'display.html', context)
