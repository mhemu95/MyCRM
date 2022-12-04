from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    description = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='client', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.name
