from django.shortcuts import render, redirect
from .models import Todo


def index(request):
    query = request.GET.get("q", "")

    todos = Todo.objects.filter(
        title__icontains=query
    )

    context = {
        "todos": todos,
    }
    return render(request, "index.html", context)


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
