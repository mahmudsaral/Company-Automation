# Generated by Django 3.1.1 on 2020-09-23 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0044_denetci_9001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='denetci_9001',
            name='Denetci_Adı',
        ),
        migrations.RemoveField(
            model_name='denetci_9001',
            name='Scope',
        ),
    ]