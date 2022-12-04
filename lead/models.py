from django.db import models
from django.contrib.auth.models import User


class Lead(models.Model):

    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    CHOICES_PRIORITY = (
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    )

    NEW = 'new'
    CONTACTED = 'contacted'
    WON = 'won'
    LOST = 'lost'

    CHOICES_STATUS = (
        ('NEW', 'New'),
        ('CONTACTED', 'Contacted'),
        ('WON', 'Won'),
        ('LOST', 'Lost'),
    )

    name = models.CharField(max_length=150)
    email = models.EmailField()
    description = models.TextField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=CHOICES_PRIORITY, default=MEDIUM)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=NEW)
    created_by = models.ForeignKey(User, related_name='lead', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    became_client = models.BooleanField(default=False)

    def __str__(self):
        return self.name
