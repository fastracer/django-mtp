# Generated by Django 3.0.3 on 2020-08-31 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sequence', '0017_transtype_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sequence',
            name='tag',
        ),
        migrations.AddField(
            model_name='sequence',
            name='tag',
            field=models.ManyToManyField(to='sequence.Tag'),
        ),
    ]
