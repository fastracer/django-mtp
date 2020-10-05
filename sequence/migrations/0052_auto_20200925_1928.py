# Generated by Django 3.0.3 on 2020-09-25 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sequence', '0051_auto_20200925_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='camera_make',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sequence.CameraMake'),
        ),
        migrations.AddField(
            model_name='image',
            name='camera_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sequence.CameraModel'),
        ),
    ]
