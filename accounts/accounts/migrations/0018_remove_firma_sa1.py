# Generated by Django 3.1.1 on 2020-09-12 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20200912_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firma',
            name='SA1',
        ),
    ]
