# Generated by Django 3.0.3 on 2020-09-02 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sequence', '0024_auto_20200901_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='icon',
            name='filename',
        ),
    ]
