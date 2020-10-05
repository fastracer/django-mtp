# Generated by Django 3.0.3 on 2020-09-26 22:03

import accounts.models
from django.db import migrations, models
import storages.backends.s3boto3


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20200913_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, storage=storages.backends.s3boto3.S3Boto3Storage(bucket=''), upload_to=accounts.models.image_directory_path),
        ),
    ]
