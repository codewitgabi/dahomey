from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("create-todo/", views.createTodo, name="create_todo"),
    path("update-todo/<int:todoId>/", views.updateTodo, name="update_todo"),
]
