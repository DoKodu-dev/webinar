from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
    class Meta:
        verbose_name_plural = 'Entries'

    title = models.CharField('Title', max_length=100)
    image = models.ImageField(upload_to='entries/')
    pub_date = models.DateTimeField('Opublikowano')
    content = models.TextField('Tekst')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

