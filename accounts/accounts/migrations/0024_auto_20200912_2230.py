# Generated by Django 3.1.1 on 2020-09-12 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20200912_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firma',
            name='nace',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
