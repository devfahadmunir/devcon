# Generated by Django 3.0.5 on 2020-05-26 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devconnector', '0012_comments_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]