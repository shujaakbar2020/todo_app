from django.shortcuts import render, redirect
from .models import Task
# Create your views here.


def index(request):
    task = Task.objects.all()

    if request.method == 'POST':
        new_task = request.POST.get('text')
        if new_task != "":
            newTask = Task(description=new_task, completed=False)
            newTask.save()
        # print(new_task)
    context = {
        'tasks': task,
    }
    return render(request, 'todo/index.html', context)


def deleteTask(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    # print(task)
    return redirect('/todo/')
