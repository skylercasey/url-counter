# Generated by Django 3.1.6 on 2021-02-08 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20210208_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domain',
            name='url',
        ),
        migrations.AddField(
            model_name='domain',
            name='url1',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
