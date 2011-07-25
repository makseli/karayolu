#*-* coding: utf-8-*-
from django.db import models
#from tck.yolnotu.models import YolNotlari
#from filebrowser.fields import FileBrowseField

class Sehirler(models.Model):
   sehir = models.CharField(max_length=32, verbose_name="SehirAdi")
#   resim = models.FileBrowseField("Image", max_length=200, directory="medya/m_iller/", extensions=[".jpg"], blank=True, null=True)
   kisa_tanitim = models.TextField(verbose_name="Kisa Tanitim")
   il_tck_kurum = models.CharField(max_length=128, verbose_name="Tck Kurum-Bolge")
   il_tck_web = models.CharField(max_length=128, verbose_name="Tck Web")
   il_tck_eposta = models.CharField(max_length=128, verbose_name="Yetkili EPosta")
   il_tck_adres = models.CharField(max_length=256, verbose_name="Adres")
   slug = models.SlugField(max_length=128, verbose_name="Url")
   
   def __unicode__(self):
    return self.sehir
    return self.il_tck_kurum
    return self.il_tck_web
    return self.il_tck_eposta
class Meta:
    verbose_name = "Şehirlerimiz"
    verbose_name_plural = "Şehirlerimiz"
class Admin:
    list_display = ("sehir", "il_tck_kurum")
    search_fields = ["sehir"]
    list_filter = ("sehir")
        
        
        
        
        
   
class Ilceler(models.Model):
    ilce_adi = models.CharField(max_length=32, verbose_name="Ilce Adi")
#    resim = models.FileBrowseField("Image", max_length=200, directory="medya/m_ilceler/", extensions=[".jpg"], blank=True, null=True)
    ilce_tanitim  = models.TextField(verbose_name="Tanitim")
    sehir = models.ForeignKey(Sehirler,verbose_name="Şehir Adi") # related_name="+", 
    slug = models.SlugField(max_length=128, verbose_name="Url")
    def unicode(self):
     return self.ilce_adi
#    return u'%s' % (self.sehir)
 
class Meta(object):
    verbose_name = "İlçelerimiz"
    verbose_name_plural = "Ilçelerimiz"
    
class Admin:
    list_display = ("ilce", "sehir", "ilce_tanitim",)
    search_fields = ["ilce", "sehir", "ilce_tanitim"]
    list_filter = ("ilce", "sehir")
    
    
    
    
    
class YolNotlari(models.Model):
    NotBaslik = models.CharField(max_length=32, verbose_name="Yol Durum Başlığı")
#    resim = models.FileBrowseField("Image", max_length=200, directory="medya/m_ilceler/", extensions=[".jpg"], blank=True, null=True)
    DurumAciklama  = models.TextField(verbose_name="Yol Durumu Açıklama")
    Tavsiye  = models.TextField(verbose_name="Durum için Tavsiye")
    DurumGecerlilik = models.CharField(max_length=128, verbose_name="Yolun Şuanki Durumu")
    ilce = models.ForeignKey(Ilceler,verbose_name="İlçe Adi") 
    sehir = models.ForeignKey(Sehirler,verbose_name="Şehir Adi") 
    slug = models.SlugField(max_length=128, verbose_name="Url")

def unicode(self):
    return self.NotBaslik
    return self.Tavsiye
    return self.DurumGecerlilik
    return self.DurumAciklama
    return self.ilce
    
class Meta:
    verbose_name = "Yol Notları"
    verbose_name_plural = "Yol Notları"
class Admin:
    list_display = ("ilce", "sehir", "Tavsiye", "NotBaslik", "DurumAciklama")
    search_fields = ["ilce", "NotBaslik"]
    list_filter = ("ilce", "NotBaslik")