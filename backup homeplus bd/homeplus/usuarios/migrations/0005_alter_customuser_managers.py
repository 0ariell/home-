# Generated by Django 5.1.5 on 2025-01-20 21:57

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
