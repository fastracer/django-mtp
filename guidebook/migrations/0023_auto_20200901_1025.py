# Generated by Django 3.0.3 on 2020-09-01 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guidebook', '0022_auto_20200831_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guidebook',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
