# Generated by Django 3.1.1 on 2020-09-18 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0035_fbf_standard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fbf',
            name='Standard',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
