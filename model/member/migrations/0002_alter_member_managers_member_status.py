# Generated by Django 5.0.2 on 2024-02-21 14:06

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='member',
            managers=[
                ('enabled_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]