# Generated by Django 3.0.3 on 2020-09-21 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guidebook', '0027_auto_20200921_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guidebook',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
