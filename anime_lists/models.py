import datetime

from django.db import models

# Create your models here.


class Titles(models.Model):
    """Название аниме"""
    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Строковое представление модели"""
        return self.text


class Entry(models.Model):
    """Описание аниме"""
    topic = models.ForeignKey(Titles, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:30]}..."
