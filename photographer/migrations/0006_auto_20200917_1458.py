# Generated by Django 3.0.3 on 2020-09-17 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photographer', '0005_auto_20200917_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photographer',
            name='image_quality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photographer.ImageQuality'),
        ),
    ]
