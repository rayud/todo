from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Todo

default_message = "to use this button, you need to login :)"

# Create your views here.

def read_more(request):
    return render(request, "crud/read_more.html")
    
@login_required(login_url='login')
def more(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'crud/more.html',{'todo': todo})

def index(request):
    todos = Todo.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(todos, 3) # show 5 todos per page

    try:
        todo_list = paginator.page(page)
    except PageNotAnInteger:
        todo_list = paginator.page(1)
    except EmptyPage:
        todo_list = paginator.page(paginator.num_pages)
    return render(request, "crud/index.html", { "todo_list": todo_list })


@require_http_methods(["POST"])
def add(request):
    if request.method == 'POST':
        note = Todo.objects.create(title=request.POST["title"], details=request.POST["details"])
        note.save()
        return redirect("index")
    else:
        return render(request, 'crud/index.html', { "todo_list": todos })

@login_required(login_url='login')
def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.title = "Task Completed" # Change the name property
    todo.save() # Save the changes to the database
    return redirect("index")

@login_required(login_url='login')
def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect("index")

@login_required(login_url='login')
def wipe(request):
    x = Todo.objects.all()
    x.delete()
    return redirect("index")

    