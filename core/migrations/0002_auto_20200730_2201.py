# Generated by Django 3.0.8 on 2020-07-31 01:01

import core.models
from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Image'),
        ),
    ]
