# Generated by Django 4.2.4 on 2023-10-14 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0038_remove_chatmessage_receiver_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='chatmessage',
            old_name='user',
            new_name='sender',
        ),
        migrations.RemoveField(
            model_name='chatmessage',
            name='thread',
        ),
        migrations.DeleteModel(
            name='Thread',
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='social.chatroom'),
            preserve_default=False,
        ),
    ]