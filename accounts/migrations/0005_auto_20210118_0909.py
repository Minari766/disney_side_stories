# Generated by Django 2.2 on 2021-01-18 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210118_0905'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='name',
            new_name='username',
        ),
    ]
