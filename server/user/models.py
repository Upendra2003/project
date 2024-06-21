from django.db import models
import uuid

# Create your models here.
class UserDetails(models.Model):
    user_id=models.UUIDField(default=uuid.uuid4,primary_key=True)
    user_name=models.CharField(max_length=100,blank=True,null=True)
    user_url = models.URLField(blank=True, null=True)
    created=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user_name