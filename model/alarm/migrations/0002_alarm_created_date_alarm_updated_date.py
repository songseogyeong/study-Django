# Generated by Django 5.0.2 on 2024-02-26 09:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alarm',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alarm',
            name='updated_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
