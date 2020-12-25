# Generated by Django 2.2.16 on 2020-12-21 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201214_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormPreviewTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Attraction', verbose_name='アトラクション')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category', verbose_name='カテゴリ')),
            ],
        ),
    ]