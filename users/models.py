from django.db import models
from vote.models import VoteModel
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)       # pole tekstowe o określonej długości
    content = models.TextField()                   # pole tekstowe o nieokreślonej długości
    published = models.BooleanField(default=False) # flaga true/false
    created = models.DateTimeField(auto_now_add=True) # data utworzenia - tylko przy utworzeniu
    modified = models.DateTimeField(auto_now=True) # data modyfikacji - zawsze gdy klikniemy save


class Entry(VoteModel, models.Model):
    class Meta:
        verbose_name_plural = 'Entries'

    title = models.CharField('Title', max_length=100)
    image = models.ImageField(upload_to='entries/')
    pub_date = models.DateTimeField('Opublikowano')
    content = models.TextField('Tekst')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

