# Generated by Django 3.1.1 on 2020-09-13 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_auto_20200912_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firma',
            name='Scope',
            field=models.TextField(max_length=200, null=True),
        ),
    ]