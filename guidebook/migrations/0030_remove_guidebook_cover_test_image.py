# Generated by Django 3.0.3 on 2020-09-26 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guidebook', '0029_auto_20200926_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guidebook',
            name='cover_test_image',
        ),
    ]
