# Generated by Django 4.1.1 on 2022-09-19 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_lectures'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='lecture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.lectures'),
        ),
    ]
