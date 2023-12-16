# Generated by Django 4.1.1 on 2022-09-19 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_lectures_activites_lectures_activites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lectures',
            name='activites',
        ),
        migrations.AddField(
            model_name='lectures',
            name='activites',
            field=models.ManyToManyField(blank=True, to='base.activity'),
        ),
    ]
