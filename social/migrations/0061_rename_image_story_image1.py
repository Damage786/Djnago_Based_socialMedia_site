# Generated by Django 4.2.4 on 2023-10-26 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0060_remove_profile_view_count_remove_profile_views'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='image',
            new_name='image1',
        ),
    ]
