# Generated by Django 2.2.5 on 2019-10-19 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='sex',
            new_name='gender',
        ),
    ]
