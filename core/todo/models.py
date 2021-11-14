from django.db import models
from account.models import UserBase


class TodoTask(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    author = models.ForeignKey(
        UserBase, on_delete=models.CASCADE, verbose_name="Автор")
    task_is_set_to = models.ManyToManyField(
        UserBase,
        related_name='user_tasks',
        blank=True,
        verbose_name="Кому поставлена задача"
    )
    created = models.DateField(auto_now_add=True, verbose_name="Створено")
    updated = models.DateField(auto_now=True, verbose_name="Оновлено")
    image = models.ImageField(
        upload_to='task_images/',
        verbose_name="Фотографія",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title
