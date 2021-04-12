from django.db import models


class Node(models.Model):
    title = models.CharField(null=False, max_length=100)
    text = models.CharField(max_length=1000)
    date = models.DateTimeField('updated at')
