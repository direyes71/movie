# Generated by Django 2.2.5 on 2019-10-20 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.Movie', verbose_name='movie'),
        ),
    ]
