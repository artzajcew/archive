from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import ArchiveFile, Folder, Tag

class ArchiveFileInline(admin.TabularInline):
    model = ArchiveFile
    extra = 0
    fields = ("title", "slug", "created_at")
    readonly_fields = ("title", "slug", "created_at")

@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ("name", "owner")
    search_fields = ("name",)
    list_filter = ("owner",)
    ordering = ("name",)
    inlines = [ArchiveFileInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "owner")
    search_fields = ("name",)
    list_filter = ("owner",)
    ordering = ("name",)


@admin.register(ArchiveFile)
class ArchiveFileAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "title_length", "owner", "folder", "created_at")
    search_fields = ("title", "description")
    list_filter = ("owner", "folder", "created_at")
    ordering = ("-created_at",)

class UserArchiveFileInline(admin.TabularInline):
    model = ArchiveFile
    extra = 0
    fields = ("title", "folder", "slug", "created_at")
    readonly_fields = ("title", "folder", "slug", "created_at")


class CustomUserAdmin(UserAdmin):
    inlines = [UserArchiveFileInline]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)