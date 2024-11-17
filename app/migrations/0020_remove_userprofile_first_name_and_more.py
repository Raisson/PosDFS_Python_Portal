# Generated by Django 5.1.2 on 2024-11-17 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_rename_name_userprofile_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='raisson', max_length=50),
        ),
    ]
