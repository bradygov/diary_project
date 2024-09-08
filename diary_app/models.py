from django.db import models

# diary_app/models.py
from django.db import models
from django.contrib.auth.models import User

class DiaryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Reply(models.Model):
    entry = models.ForeignKey(DiaryEntry, on_delete=models.CASCADE)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reply by {self.user.username} on {self.entry.title}'