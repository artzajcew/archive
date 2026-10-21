from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import ArchiveFile, Folder


class ArchiveTests(TestCase):
    def test_user_sees_only_own_files(self):
        first = User.objects.create_user("first", password="pass12345")
        second = User.objects.create_user("second", password="pass12345")
        folder = Folder.objects.create(owner=first, name="Документы")
        ArchiveFile.objects.create(owner=first, folder=folder, title="Мой файл", file="a.txt")
        ArchiveFile.objects.create(owner=second, title="Чужой файл", file="b.txt")

        self.client.force_login(first)
        response = self.client.get(reverse("archive:list"))

        self.assertContains(response, "Мой файл")
        self.assertNotContains(response, "Чужой файл")
