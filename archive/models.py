from django.conf import settings
from django.db import models
from django.db.models.functions import Length
from django.urls import reverse
from django.utils.text import slugify

class Folder(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец")
    name = models.CharField("Название", max_length=100)

    class Meta:
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(fields=["owner", "name"], name="unique_folder_owner_name")
        ]
        verbose_name = "Папка"
        verbose_name_plural = "Папки"

    def __str__(self):
        return self.name

class Tag(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец")
    name = models.CharField("Название", max_length=40)

    class Meta:
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(fields=["owner", "name"], name="unique_tag_owner_name")
        ]
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name


class ArchiveFile(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец")
    folder = models.ForeignKey(Folder, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Папка")
    title = models.CharField("Название", max_length=200)
    description = models.TextField("Описание", blank=True)
    file = models.FileField("Файл", upload_to="archive/%Y/%m/")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Теги")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    slug = models.SlugField("Слаг", max_length=200, unique=True, null=True, blank=True)
    title_length = models.GeneratedField(
        expression=Length("title"),
        output_field=models.IntegerField("Длина названия"),
        db_persist=True,
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title) or "file"
            slug = base_slug
            number = 2

            while ArchiveFile.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{number}"
                number += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("archive:detail", kwargs={"slug": self.slug})
