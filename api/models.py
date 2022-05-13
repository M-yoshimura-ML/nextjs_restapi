from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=56)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + "-" + self.title


class Task(models.Model):
    title = models.CharField(max_length=56)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + "-" + self.title

