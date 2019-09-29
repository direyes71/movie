# Generated by Django 2.2.5 on 2019-09-28 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20190928_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='title',
        ),
        migrations.AddField(
            model_name='movie',
            name='name',
            field=models.CharField(default='', max_length=340, verbose_name='name'),
            preserve_default=False,
        ),
    ]
