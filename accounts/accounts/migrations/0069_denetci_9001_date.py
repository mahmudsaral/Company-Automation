# Generated by Django 3.1.1 on 2020-10-06 11:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0068_kontrol_personel_adı'),
    ]

    operations = [
        migrations.AddField(
            model_name='denetci_9001',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
