# Generated by Django 5.0.7 on 2024-09-01 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_fotografia_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='publicado',
            field=models.BooleanField(default=False),
        ),
    ]
