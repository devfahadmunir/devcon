# Generated by Django 3.0.5 on 2020-06-15 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devconnector', '0037_posts_liked_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='disliked',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='liked',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='liked_users',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='likes',
        ),
    ]