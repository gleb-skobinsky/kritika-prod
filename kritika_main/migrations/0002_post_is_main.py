# Generated by Django 4.1.2 on 2023-01-25 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kritika_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]