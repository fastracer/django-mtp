# Generated by Django 3.0.3 on 2020-09-25 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sequence', '0050_auto_20200925_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='camera_make',
        ),
        migrations.RemoveField(
            model_name='image',
            name='camera_model',
        ),
    ]
