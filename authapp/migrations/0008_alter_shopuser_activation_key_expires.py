# Generated by Django 3.2.10 on 2022-02-05 15:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('authapp', '0007_auto_20220205_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 7, 15, 27, 51, 833655, tzinfo=utc)),
        ),
    ]
