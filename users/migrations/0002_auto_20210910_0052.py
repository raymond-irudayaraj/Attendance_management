# Generated by Django 3.2.7 on 2021-09-09 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='course',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='grade',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
