# Generated by Django 2.0.2 on 2018-03-03 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0012_auto_20180223_2153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-pub_date',)},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-pub_date',)},
        ),
    ]
