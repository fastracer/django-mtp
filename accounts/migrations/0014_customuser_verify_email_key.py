# Generated by Django 3.0.3 on 2020-07-22 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20200722_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='verify_email_key',
            field=models.CharField(default='', max_length=100),
        ),
    ]