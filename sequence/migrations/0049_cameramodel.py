# Generated by Django 3.0.3 on 2020-09-25 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sequence', '0048_labeltype_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='CameraModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
