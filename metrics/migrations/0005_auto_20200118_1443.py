# Generated by Django 3.0.2 on 2020-01-18 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0004_auto_20200118_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='text',
            field=models.CharField(default='Your goal here>', max_length=40),
        ),
        migrations.AlterField(
            model_name='goal',
            name='user',
            field=models.CharField(default='unknown user', max_length=50),
        ),
    ]