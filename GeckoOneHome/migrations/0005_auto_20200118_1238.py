# Generated by Django 3.0.2 on 2020-01-18 12:38

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeckoOneHome', '0004_myuser_date_of_birth'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='myuser',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(default=models.EmailField(max_length=255, unique=True, verbose_name='email address'), max_length=40),
        ),
    ]