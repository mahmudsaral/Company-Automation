# Generated by Django 3.1.1 on 2020-09-10 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200911_0054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='firma',
            old_name='firma_adi',
            new_name='Company_Name',
        ),
    ]
