# Generated by Django 3.1.1 on 2020-09-20 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0038_remove_fbf_kapsam'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]