# Generated by Django 5.1.2 on 2024-11-17 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_remove_userprofile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]