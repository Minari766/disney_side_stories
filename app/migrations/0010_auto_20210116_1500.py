# Generated by Django 2.2 on 2021-01-16 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='article',
            new_name='post',
        ),
    ]
