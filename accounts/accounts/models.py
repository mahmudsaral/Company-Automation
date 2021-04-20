from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from datetime import datetime
from datetime import timedelta


class firma(models.Model):
     
     CertNo = models.CharField(max_length=200, null=True)
     Company_Name = models.TextField (max_length=200, null=True)
     Standard = models.IntegerField(null=True)
     CA_Date = models.DateField(blank=True)
     SA1 = models.DateField(null=True, blank=True)
     SA2 = models.DateField(null=True, blank=True)
     ReReg = models.DateField(null=True, blank=True)
     Suspension_Date = models.DateField(null=True, blank=True)
     Withdrawal_Date = models.DateField(null=True, blank=True)
     Address = models.TextField (max_length=200,null=True)
     Yetkili_Kisi = models.CharField(max_length=100,null=True)
     Scope = models.TextField(max_length=200,null=True)
     Phone = models.IntegerField(null=True)
     Fax = models.IntegerField(null=True)
     email = models.CharField(max_length=200,null=True)
     ea = models.CharField(max_length=200,null=True)
     nace = models.CharField(max_length=200,null=True,blank=True)
     Initial_Cert_Date = models.DateField(null=True, blank=True)
     Cert_Date = models.DateField(null=True, blank=True)
     belge_bitiş_tarihi = models.DateField(null=True, blank=True)
     created = models.DateField(auto_now=True)
     updated = models.DateField(auto_now=True)
     


     def __str__(self):
          return self.Company_Name

firmas = models.ForeignKey(firma, null=True, on_delete= models.SET_NULL)
class Order(models.Model):
     STATUS = (
               ('Pending', 'Pending'),
               ('Out for delivery', 'Out for delivery'),
               ('Delivered', 'Delivered'),
               )

     firma = models.CharField(max_length=200, null=True)
     date_created = models.DateTimeField(auto_now_add=True, null=True)
     status = models.CharField(max_length=200, null=True, choices=STATUS)

class fbf(models.Model):
     Company_Name = models.TextField (max_length=200, null=True)
     Address = models.TextField (max_length=200,null=True)
     ilgili_kişi = models.CharField(max_length=100,null=True)
     Telefon	= models.IntegerField(null=True)
     Email = models.CharField(max_length=200,null=True)
     Vergi_Dairesi = models.CharField(max_length=100,null=True)
     Ünvanı = models.CharField(max_length=100,null=True)
     Faks = models.IntegerField(null=True)
     Web	=  models.CharField(max_length=100,null=True,blank=True)
     Vergi_No = models.IntegerField(null=True,blank=True)
     Yönetici_Sayısı	= models.IntegerField(null=True,blank=True)
     Kritik_İşçi_Sayısı= models.IntegerField(null=True,blank=True)
     Tekrarlı_İşler_Yürüten_Personel_Sayısı = models.IntegerField(null=True,blank=True)
     Toplam_Çalışan_Sayısı = models.IntegerField(null=True,blank=True)
     Çalışma_Saatleri = models.CharField(max_length=100,null=True,blank=True)
     Gerçekleştirilen_Süreçler = models.CharField(max_length=100,null=True,blank=True)
     HİZMET_VERDİĞİNİZ_SEKTÖRLER_SAĞLAMIŞ_OLDUĞUNUZ_ÜRÜN_HİZMETLER_İLE_İLGİLİ_ÖRNEKLER =  models.CharField(max_length=100,null=True,blank=True)		
     PROSES_VE_FAALİYETLERİNİZ_İNSAN_VE_TEKNİK_KAYNAKLAR_FONKSİYONLAR = models.CharField(max_length=100,null=True,blank=True)
     HARİÇ_TUTMALAR_ve_GEREKÇELER =  models.CharField(max_length=100,null=True,blank=True)
     YASAL_ŞARTLAR  =  models.CharField(max_length=100,null=True,blank=True)
     DIŞ_KAYNAKLI_SÜREÇLER  =  models.CharField(max_length=100,null=True,blank=True)
     VARSA_MEVCUT_ÜRÜN_SİSTEM_BELGELERİ	=  models.CharField(max_length=100,null=True,blank=True)
     BELGELENDİRME_KAPSAMINIZ =  models.TextField(max_length=200,null=True,blank=True)
     Kiwadan_Nasıl_Haberdar_Oldunuz  =  models.CharField(max_length=100,null=True,blank=True)
     Danışmanlık_Hzmt_Aldınız_mı =  models.CharField(max_length=100,null=True,blank=True)
     Formu_Dolduran =  models.CharField(max_length=100,null=True,blank=True)
     Tarih = models.DateField(null=True, blank=True)
     Standard = models.CharField(max_length=100,null=True,blank=True)
     ea = models.CharField(max_length=200,null=True , blank=True)
     
     
     def __str__(self):
          return self.Company_Name



class Denetci_9001(models.Model):

     
     Cert = models.IntegerField(null=True)
     Personel_Adı = models.TextField (max_length=200, null=True)
     ea = models.CharField(max_length=200,null=True)
     denetim_suresi = models.IntegerField(null=True,blank=True)
     def __str__(self):
          return str(self.Personel_Adı)
     

class Event(models.Model):
     
     user = models.ForeignKey(User,related_name='User',null=True, on_delete=models.CASCADE)
     Scope = models.CharField(max_length=100,null=True)
     Personel_Adı = models.ForeignKey(Denetci_9001, null=True,on_delete=models.SET_NULL)
     description = models.TextField()
     start_time = models.DateTimeField()
     end_time = models.DateTimeField()
     created_date = models.DateTimeField(auto_now_add=True)
     

     def str(self):
          return self.Personel_Adı

     def get_absolute_url(self):
          return reverse('event-detail', args=(self.id,))

     @property
     def get_html_url(self):
          url = reverse('event-detail', args=(self.id,))
          return f'<a href="{url}"> {self.Personel_Adı} </a>'

class kontrol(models.Model):

     Personel_Adı = models.ForeignKey(Denetci_9001, null=True,on_delete=models.SET_NULL)
     end_time = models.ForeignKey(Event,null=True,on_delete=models.SET_NULL,default=datetime)
     date = models.DateTimeField(default=datetime.now, blank=True)
     date1 = models.DateTimeField(default=datetime.now, blank=True)

     @property
     def is_open(self):
        now = datetime.now().time()
        return  now 
     def __str__(self):
          return format(self.end_time)


class EventMember(models.Model):

     event = models.ForeignKey(Event, related_name='Event',null=True,on_delete=models.CASCADE)
     Personel_Adı = models.ForeignKey(Denetci_9001, null=True,on_delete=models.SET_NULL)

   
     class Meta:
          unique_together = ['event','Personel_Adı']