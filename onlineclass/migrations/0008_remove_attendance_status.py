# Generated by Django 3.2.7 on 2021-09-10 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlineclass', '0007_auto_20210910_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='status',
        ),
    ]
