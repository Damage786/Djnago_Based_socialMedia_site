# Generated by Django 4.2.4 on 2023-09-04 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0010_remove_post_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Like',
        ),
    ]