# Generated by Django 4.2.4 on 2023-10-06 15:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0026_rename_photo_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='post_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
