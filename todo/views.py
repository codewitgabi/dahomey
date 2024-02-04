from django.shortcuts import render, redirect
from django_ratelimit.decorators import ratelimit
from .models import Todo
from .forms import TodoForm


def index(request):
    query = request.GET.get("q", "")

    todos = Todo.objects.filter(
        title__icontains=query
    )

    context = {
        "todos": todos,
    }
    return render(request, "index.html", context)


@ratelimit(key="ip", rate="5/m")
def createTodo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        # create todo <ModelName>.objects.create(*fields)
        Todo.objects.create(
            title=title,
            content=content
        )

        return redirect("index")

    return render(request, "create-todo.html")


def updateTodo(request, todoId):
    todo = Todo.objects.get(id=todoId)

    form = TodoForm(instance=todo)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)

        if form.is_valid:
            form.save()
            
            return redirect("index")

    return render(request, "update-todo.html", {"form": form})

