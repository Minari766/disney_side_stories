# Generated by Django 2.2 on 2021-01-22 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210122_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='アイコン'),
        ),
    ]