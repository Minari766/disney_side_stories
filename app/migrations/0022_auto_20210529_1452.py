# Generated by Django 2.2 on 2021-05-29 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_post_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='public',
            field=models.BooleanField(default=False, verbose_name='公開フラグ'),
        ),
    ]
