from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import RegisterUser

@receiver(post_save, sender=User)
def create_register(sender, instance, created, **kwargs):
    if created:
        RegisterUser.objects.create(
            user=instance,
            email=instance.email
        )
        print(f"New user created: {instance.username}")


@receiver(post_delete, sender=User)
def delete_register(sender, instance, **kwargs):
    try:
        register_user = RegisterUser.objects.get(user=instance)
        register_user.delete()
        print(f"RegisterUser deleted for user: {instance.username}")
    except RegisterUser.DoesNotExist:
        pass  

@receiver(post_delete, sender=RegisterUser)
def delete_user(sender, instance, **kwargs):
    try:
        user = instance.user 
        user.delete()
        print(f"User deleted for RegisterUser: {user.username}")
    except User.DoesNotExist:
        pass