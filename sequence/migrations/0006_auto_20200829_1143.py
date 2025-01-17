# Generated by Django 3.0.3 on 2020-08-29 08:43

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sequence', '0005_auto_20200829_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transporttype',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='transporttype',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='sequence.TransportType'),
        ),
    ]
