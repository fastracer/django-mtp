# Generated by Django 3.0.3 on 2020-09-18 07:34

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sequence', '0035_auto_20200916_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('accuracy', models.FloatField(default=0)),
                ('altitude', models.FloatField(default=0)),
                ('direction', models.FloatField(default=0)),
                ('first_seen_at', models.DateTimeField(blank=True, null=True)),
                ('mf_key', models.CharField(blank=True, max_length=100, null=True)),
                ('last_seen_at', models.DateTimeField(blank=True, null=True)),
                ('layer', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=100)),
                ('geometry_type', models.CharField(default='Point', max_length=50)),
                ('geometry_point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='MapFeatureDetection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_key', models.CharField(blank=True, max_length=100, null=True)),
                ('detection_key', models.CharField(blank=True, max_length=100, null=True)),
                ('user_key', models.CharField(blank=True, max_length=100, null=True)),
                ('mf_key', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]