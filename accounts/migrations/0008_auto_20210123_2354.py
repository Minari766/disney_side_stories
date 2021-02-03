# Generated by Django 2.2 on 2021-01-23 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210122_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(default=1, max_length=30, verbose_name='姓'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(default=1, max_length=30, verbose_name='名'),
            preserve_default=False,
        ),
    ]