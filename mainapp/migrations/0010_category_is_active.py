# Generated by Django 3.2.10 on 2022-01-26 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активно'),
        ),
    ]