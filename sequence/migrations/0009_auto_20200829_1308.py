# Generated by Django 3.0.3 on 2020-08-29 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sequence', '0008_auto_20200829_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transtype',
            name='icon',
            field=models.CharField(default='', max_length=50),
        ),
    ]
