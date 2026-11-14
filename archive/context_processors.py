from .models import ArchiveFile, Folder, Tag


def archive_context(request):
    if not request.user.is_authenticated:
        return {}

    return {
        "archive_files_count": ArchiveFile.objects.filter(owner=request.user).count(),
        "archive_folders_count": Folder.objects.filter(owner=request.user).count(),
        "archive_tags_count": Tag.objects.filter(owner=request.user).count(),
    }