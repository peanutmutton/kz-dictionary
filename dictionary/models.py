from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Word(models.Model):
    word = models.CharField(max_length=33) #qanaghat
    definition = models.TextField(max_length=330)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word