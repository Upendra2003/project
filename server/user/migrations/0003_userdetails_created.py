# Generated by Django 5.0.6 on 2024-06-14 11:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_userdetails_id_userdetails_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]