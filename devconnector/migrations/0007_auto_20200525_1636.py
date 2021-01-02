# Generated by Django 3.0.5 on 2020-05-25 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devconnector', '0006_developer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='skills',
            field=models.CharField(choices=[('skills', 'Select Your skills'), ('html', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], default='skills', max_length=6),
        ),
    ]