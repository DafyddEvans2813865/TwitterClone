# Generated by Django 5.0.4 on 2024-05-04 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tclone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(blank=True, related_name='followed_by', to='Tclone.profile'),
        ),
    ]
