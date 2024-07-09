from django.shortcuts import render, redirect
from .models import ToDo
from .forms import ToDoForm, UpdateToDoForm

def main(request):
    # all tasks
    todos = ToDo.objects.all()

    # adding new tasks
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save() # saved
            return redirect('todo')  # redirect to home
    else:
        form = ToDoForm() # empty form

    # search
    search_query = request.POST.get('search', '')
    if search_query:
        todos = todos.filter(task__icontains=search_query) # filtering based on input


    return render(request, 'todo/main.html', {'form': form, 'todos': todos})

def remove(request, item_id):
    # checking if task exists
    try:
        item = ToDo.objects.get(id=item_id)
        item.delete()
    except ToDo.DoesNotExist:
        pass
    return redirect('todo')

def edit(request, item_id): 
    # check if it exists if it doesn't redirect
    try:
        todo = ToDo.objects.get(id=item_id)
    except ToDo.DoesNotExist:
        return redirect('todo')
    
    # editing
    if request.method == 'POST':
        form = UpdateToDoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo')
    else:
        form = UpdateToDoForm(instance=todo)
    
    return render(request, 'todo/edit.html', {'form': form, 'todos': todo})

def is_complete(request, item_id):
    try:
        # is task completed or not
        todo = ToDo.objects.get(id=item_id)
        todo.check_complete()
    except ToDo.DoesNotExist:
        pass
    return redirect('todo')
