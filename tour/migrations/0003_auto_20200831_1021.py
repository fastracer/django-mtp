# Generated by Django 3.0.3 on 2020-08-31 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0002_auto_20200831_1001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour',
            old_name='tag',
            new_name='tour_tag',
        ),
    ]
