# Generated by Django 4.1.1 on 2022-09-19 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_remove_lectures_activities_alter_activity_lecture'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]
