from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    COLOR_CHOICES = [
        ('white', 'White'),
        ('yellow', 'Yellow'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('pink', 'Pink'),
        ('purple', 'Purple'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=200)
    content = models.TextField()
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='white')
    is_pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_pinned', '-updated_at']

    def __str__(self):
        return self.title
