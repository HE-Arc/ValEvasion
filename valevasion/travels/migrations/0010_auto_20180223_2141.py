# Generated by Django 2.0.2 on 2018-02-23 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0009_auto_20180222_2218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='author',
        ),
    ]
