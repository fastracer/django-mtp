# Generated by Django 3.0.3 on 2020-09-15 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guidebook', '0024_auto_20200901_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='scene',
            name='start_x',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='scene',
            name='start_y',
            field=models.FloatField(default=0),
        ),
    ]
