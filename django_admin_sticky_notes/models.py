from django.db import models


class StickyNote(models.Model):
    body = models.TextField()
