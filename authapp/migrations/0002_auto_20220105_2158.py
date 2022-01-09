# Generated by Django 3.2.10 on 2022-01-05 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveIntegerField(verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='avatar',
            field=models.ImageField(default='avatar/default_profile_photo.png', upload_to='avatar', verbose_name='Фото профиля'),
        ),
    ]