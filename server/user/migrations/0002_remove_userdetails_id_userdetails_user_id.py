# Generated by Django 5.0.6 on 2024-06-14 11:52

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='id',
        ),
        migrations.AddField(
            model_name='userdetails',
            name='user_id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]