# Generated by Django 3.1.1 on 2020-10-02 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0055_denetci_9001_denetim_suresi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='Denetçi_Adı',
        ),
        migrations.AddField(
            model_name='event',
            name='Personel_Adı',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.denetci_9001'),
        ),
    ]
