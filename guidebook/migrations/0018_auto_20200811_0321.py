# Generated by Django 3.0.3 on 2020-08-11 02:21

from django.db import migrations, models
import guidebook.models


class Migration(migrations.Migration):

    dependencies = [
        ('guidebook', '0017_auto_20200806_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guidebook',
            name='cover_image',
            field=models.ImageField(null=True, upload_to=guidebook.models.image_directory_path),
        ),
    ]
