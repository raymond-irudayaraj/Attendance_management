# Generated by Django 3.2.7 on 2021-09-10 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlineclass', '0002_auto_20210910_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='is_active',
        ),
    ]
