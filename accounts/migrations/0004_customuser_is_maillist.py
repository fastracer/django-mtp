# Generated by Django 3.0.3 on 2020-07-19 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200715_0232'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_maillist',
            field=models.BooleanField(default=False),
        ),
    ]
