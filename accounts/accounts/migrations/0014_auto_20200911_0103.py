# Generated by Django 3.1.1 on 2020-09-10 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20200911_0055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='firma',
            old_name='belgelendirme_denetim_tarihi',
            new_name='CA_Date',
        ),
        migrations.RenameField(
            model_name='firma',
            old_name='adt1',
            new_name='SA1',
        ),
        migrations.RenameField(
            model_name='firma',
            old_name='adt2',
            new_name='SA2',
        ),
        migrations.RenameField(
            model_name='firma',
            old_name='standart',
            new_name='Standard',
        ),
    ]