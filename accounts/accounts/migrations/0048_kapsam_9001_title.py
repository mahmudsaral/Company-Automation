# Generated by Django 3.1.1 on 2020-09-23 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0047_auto_20200923_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='kapsam_9001',
            name='title',
            field=models.CharField(choices=[('ISO 9001', 'ISO 9001'), ('ISO 14001', 'ISO 14001'), ('ISO 27001', 'ISO 27001'), ('ISO 45001', 'ISO 450001')], max_length=100, null=True),
        ),
    ]
