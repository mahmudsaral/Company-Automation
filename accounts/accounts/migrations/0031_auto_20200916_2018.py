# Generated by Django 3.1.1 on 2020-09-16 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_fbf'),
    ]

    operations = [
        migrations.AddField(
            model_name='fbf',
            name='Address',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='fbf',
            name='Email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='fbf',
            name='Faks',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='fbf',
            name='Gerçekleştirilen_Süreçler',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fbf',
            name='Kritik_İşçi_Sayısı',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fbf',
            name='Tekrarlı_İşler_Yürüten_Personel_Sayısı',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fbf',
            name='Telefon',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='fbf',
            name='Toplam_Çalışan_Sayısı',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fbf',
            name='Vergi_Dairesi',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fbf',
            name='Vergi_No',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fbf',
            name='Web',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fbf',
            name='Yönetici_Sayısı',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fbf',
            name='ilgili_kişi',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fbf',
            name='Çalışma_Saatleri',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fbf',
            name='Ünvanı',
            field=models.CharField(max_length=100, null=True),
        ),
    ]