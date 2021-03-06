# Generated by Django 2.1.2 on 2018-11-26 11:00

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20181115_2217'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AddField(
            model_name='user',
            name='profile_photo',
            field=models.FileField(blank=True, null=True, upload_to=api.models.file_upload_path),
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('username',), ('email',)},
        ),
    ]
