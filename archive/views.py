from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import ArchiveFileForm, FolderForm, TagForm
from .models import ArchiveFile, Folder, Tag


def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("archive:list")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def file_list(request):
    files = ArchiveFile.objects.filter(owner=request.user).select_related("folder").prefetch_related("tags")
    query = request.GET.get("q", "").strip()
    folder_id = request.GET.get("folder", "")
    tag_id = request.GET.get("tag", "")
    if query:
        files = files.filter(Q(title__icontains=query) | Q(description__icontains=query))
    if folder_id:
        files = files.filter(folder_id=folder_id)
    if tag_id:
        files = files.filter(tags__id=tag_id)
    context = {
        "files": files.distinct(),
        "folders": Folder.objects.filter(owner=request.user),
        "tags": Tag.objects.filter(owner=request.user),
        "query": query,
    }
    return render(request, "archive/list.html", context)


@login_required
def file_detail(request, pk):
    item = get_object_or_404(ArchiveFile.objects.prefetch_related("tags"), pk=pk, owner=request.user)
    return render(request, "archive/detail.html", {"item": item})


@login_required
def file_create(request):
    form = ArchiveFileForm(request.POST or None, request.FILES or None)
    form.fields["folder"].queryset = Folder.objects.filter(owner=request.user)
    form.fields["tags"].queryset = Tag.objects.filter(owner=request.user)
    if form.is_valid():
        item = form.save(commit=False)
        item.owner = request.user
        item.save()
        form.save_m2m()
        messages.success(request, "Файл добавлен в архив.")
        return redirect("archive:list")
    return render(request, "archive/form.html", {"form": form, "title": "Добавить файл"})


@login_required
def file_edit(request, pk):
    item = get_object_or_404(ArchiveFile, pk=pk, owner=request.user)
    form = ArchiveFileForm(request.POST or None, request.FILES or None, instance=item)
    form.fields["folder"].queryset = Folder.objects.filter(owner=request.user)
    form.fields["tags"].queryset = Tag.objects.filter(owner=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, "Изменения сохранены.")
        return redirect("archive:detail", pk=item.pk)
    return render(request, "archive/form.html", {"form": form, "title": "Изменить файл"})


@login_required
@require_POST
def file_delete(request, pk):
    item = get_object_or_404(ArchiveFile, pk=pk, owner=request.user)
    item.delete()
    messages.success(request, "Файл удалён.")
    return redirect("archive:list")


@login_required
def folder_create(request):
    form = FolderForm(request.POST or None)
    if form.is_valid():
        folder = form.save(commit=False)
        folder.owner = request.user
        folder.save()
        return redirect("archive:create")
    return render(request, "archive/form.html", {"form": form, "title": "Новая папка"})


@login_required
def tag_create(request):
    form = TagForm(request.POST or None)
    if form.is_valid():
        tag = form.save(commit=False)
        tag.owner = request.user
        tag.save()
        return redirect("archive:create")
    return render(request, "archive/form.html", {"form": form, "title": "Новый тег"})
