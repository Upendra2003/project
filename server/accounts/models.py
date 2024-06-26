from django.db import models
from django.contrib.auth.models import User
import uuid

class RegisterUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    register_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username if self.user else "No Username"
