# Generated by Django 3.0.2 on 2020-01-18 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeckoOneHome', '0003_auto_20200118_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
