# Generated by Django 5.1.2 on 2024-11-04 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_userprofile_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phone_number',
        ),
    ]