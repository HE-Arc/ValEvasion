# Generated by Django 2.0.2 on 2018-02-16 10:55

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0003_auto_20180215_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
