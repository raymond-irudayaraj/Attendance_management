# Generated by Django 3.2.7 on 2021-09-09 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210910_0259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_student',
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.IntegerField(default=True),
        ),
    ]
