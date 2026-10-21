from django import forms
from .models import ArchiveFile, Folder, Tag


class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ["name"]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]


class ArchiveFileForm(forms.ModelForm):
    class Meta:
        model = ArchiveFile
        fields = ["title", "description", "folder", "tags", "file"]
        widgets = {"description": forms.Textarea(attrs={"rows": 4})}
