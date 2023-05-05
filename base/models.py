from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, default='')
    content = models.CharField(max_length=300, default='')
    finished = models.BooleanField(default=False, blank=True)
    cData = models.CharField(null=True, blank=True, max_length=15)
    fData = models.CharField(null=True, blank=True, max_length=15)

    def __str__(self):
        return f'Title : {self.title}'
