# Generated by Django 3.0.3 on 2020-08-04 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guidebook', '0012_auto_20200804_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='scene',
            name='lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='scene',
            name='lng',
            field=models.FloatField(default=0),
        ),
    ]