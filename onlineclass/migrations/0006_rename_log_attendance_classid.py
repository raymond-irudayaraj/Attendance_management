# Generated by Django 3.2.7 on 2021-09-10 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlineclass', '0005_rename_schedule_attendance_log'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='log',
            new_name='classid',
        ),
    ]