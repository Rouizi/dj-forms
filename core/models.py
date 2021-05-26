from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    activate = models.BooleanField(default=False)
    author = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    
    def __str__(self):
        return self.title
