# Generated by Django 3.0.3 on 2020-08-30 18:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sequence', '0014_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='icon',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
