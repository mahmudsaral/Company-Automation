# Generated by Django 3.1.1 on 2020-09-23 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0043_remove_event_denetçi_adı'),
    ]

    operations = [
        migrations.CreateModel(
            name='Denetci_9001',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Scope', models.CharField(max_length=100, null=True)),
                ('Denetci_Adı', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]