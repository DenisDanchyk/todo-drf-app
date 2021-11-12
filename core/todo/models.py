from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class TodoTask(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Автор")
    task_is_set_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_tasks',
        null=True,
        blank=True,
        verbose_name="Кому поставлена задача"
    )
    created = models.DateField(auto_now_add=True, verbose_name="Створено")
    updated = models.DateField(auto_now=True, verbose_name="Оновлено")
    image = models.ImageField(
        upload_to='task_images/',
        verbose_name="Фотографія",
        null=True
    )

    def __str__(self):
        return self.title
