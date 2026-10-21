from django.contrib import admin
from .models import ArchiveFile, Folder, Tag

admin.site.register([ArchiveFile, Folder, Tag])
