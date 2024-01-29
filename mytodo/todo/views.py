from django.shortcuts import redirect, render
from .models import Todo  # Assuming your model is named Todo

def todolist(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html',{"todos":todos})

def create_todo(request):
    if request.method == "POST":
        task = request.POST.get('title')  # Fix the typo here ('tite' to 'title')
        description = request.POST.get('description')
        Todo.objects.create(task=task, description=description)

    return redirect('todolist')
def complete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todolist')
def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todolist')