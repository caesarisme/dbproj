# Generated by Django 2.2.7 on 2019-11-25 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='title',
            new_name='title_eng',
        ),
        migrations.RenameField(
            model_name='speciality',
            old_name='title',
            new_name='title_eng',
        ),
        migrations.RenameField(
            model_name='university',
            old_name='title',
            new_name='title_eng',
        ),
    ]
