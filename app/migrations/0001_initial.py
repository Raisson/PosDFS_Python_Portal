# Generated by Django 5.1.2 on 2024-10-29 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlo', models.CharField(max_length=100)),
                ('noticia', models.TextField()),
            ],
        ),
    ]
