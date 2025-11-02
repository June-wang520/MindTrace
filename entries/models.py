from django.db import models
from django.contrib.auth.models import User




class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    想做 = models.TextField(blank=True, null=True)
    所得 = models.TextField(blank=True, null=True)
    更好 = models.TextField(blank=True, null=True)
    生理 = models.TextField(blank=True, null=True)
    情绪 = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    audio = models.FileField(upload_to='audio/', blank=True, null=True)
    想做完成 = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.date}"
class Todo(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.content}"

