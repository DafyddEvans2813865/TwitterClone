# Generated by Django 5.0.4 on 2024-05-06 17:24

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tclone', '0002_alter_profile_follows'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='data_modified',
            field=models.DateTimeField(auto_now=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]