# Generated by Django 3.0.3 on 2020-08-14 23:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_mapillaryuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapillaryuser',
            name='iamges_total_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mapillaryuser',
            name='sequences_total_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mapillaryuser',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
