# Generated by Django 3.0.3 on 2020-08-30 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sequence', '0015_icon_unique_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transtype',
            name='icon',
        ),
    ]
