# Generated by Django 4.1.1 on 2022-09-17 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_products_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='gifLink',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
