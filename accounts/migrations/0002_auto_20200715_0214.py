# Generated by Django 3.0.8 on 2020-07-14 23:14
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.IntegerField(default=0),
        ),
    ]