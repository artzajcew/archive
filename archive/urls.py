from django.urls import path
from . import views

app_name = "archive"

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("archive/", views.file_list, name="list"),
    path("archive/add/", views.file_create, name="create"),
    path("archive/<int:pk>/", views.file_detail, name="detail"),
    path("archive/<int:pk>/edit/", views.file_edit, name="edit"),
    path("archive/<int:pk>/delete/", views.file_delete, name="delete"),
    path("folders/add/", views.folder_create, name="folder_create"),
    path("tags/add/", views.tag_create, name="tag_create"),
]
