# Generated by Django 3.1.1 on 2020-09-10 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_delete_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='firma',
            old_name='certno',
            new_name='Certno',
        ),
    ]