# Generated by Django 3.0.3 on 2020-09-21 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guidebook', '0026_guidebook_cover_test_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scene',
            name='start_x',
            field=models.FloatField(default=0.5),
        ),
        migrations.AlterField(
            model_name='scene',
            name='start_y',
            field=models.FloatField(default=0.5),
        ),
    ]
