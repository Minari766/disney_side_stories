# Generated by Django 2.2.16 on 2020-12-13 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201213_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Image画像'),
        ),
    ]
