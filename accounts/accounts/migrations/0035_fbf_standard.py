# Generated by Django 3.1.1 on 2020-09-18 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0034_auto_20200918_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='fbf',
            name='Standard',
            field=models.IntegerField(null=True),
        ),
    ]
