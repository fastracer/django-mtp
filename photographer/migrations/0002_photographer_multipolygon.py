# Generated by Django 3.0.3 on 2020-09-07 14:06

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photographer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographer',
            name='multipolygon',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326),
        ),
    ]
