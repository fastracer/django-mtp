# Generated by Django 3.0.3 on 2020-08-04 07:49

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guidebook', '0011_auto_20200802_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='scene',
            name='sort',
            field=models.IntegerField(default=1, null=True),
        ),
    ]