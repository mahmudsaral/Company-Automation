# Generated by Django 3.1.1 on 2020-10-04 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0063_auto_20201004_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='abc',
        ),
    ]
