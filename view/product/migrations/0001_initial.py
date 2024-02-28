# Generated by Django 5.0.2 on 2024-02-28 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_price', models.IntegerField()),
                ('product_stock', models.IntegerField()),
            ],
            options={
                'db_table': 'tbl_product',
                'ordering': ['-id'],
            },
        ),
    ]
