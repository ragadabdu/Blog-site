from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    keyword = models.TextField(max_length=255)
    view_count = models.FloatField(default=0)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

