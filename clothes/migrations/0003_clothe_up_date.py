# Generated by Django 2.1.3 on 2020-09-26 00:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0002_auto_20200926_0526'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothe',
            name='up_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
