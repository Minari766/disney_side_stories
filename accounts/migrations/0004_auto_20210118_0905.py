# Generated by Django 2.2 on 2021-01-18 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='last_name',
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(default=1, max_length=30, verbose_name='ニックネーム'),
            preserve_default=False,
        ),
    ]
