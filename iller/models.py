#*-* coding: utf-8-*-
from django.db import models

class Sehirler(models.Model):
    sehir = models.CharField(max_length=32, verbose_name="SehirAdi")
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
    ilce_tanitim  = models.TextField(verbose_name="Tanitim")
    sehir = models.ForeignKey(Sehirler) 
    slug = models.SlugField(max_length=128, verbose_name="Url")
    
    def __unicode__(self):
        return self.ilce_adi
        return self.sehir
 
    class Meta(object):
        verbose_name = "İlçelerimiz"
        verbose_name_plural = "Ilçelerimiz"
    
    class Admin:
        list_display = ("ilce", "sehir", "ilce_tanitim",)
        search_fields = ["ilce", "sehir", "ilce_tanitim"]
        list_filter = ("ilce", "sehir")
    
    
    
    
    
class YolNotlari(models.Model):
    NotBaslik = models.CharField(max_length=32, verbose_name="Yol Durum Başlığı")
    DurumAciklama  = models.TextField(verbose_name="Yol Durumu Açıklama")
    Tavsiye  = models.TextField(verbose_name="Durum için Tavsiye")
    MapLokeysin = models.TextField(max_length=128, verbose_name="Yol Google Map Koordinatları")
    DurumGecerlilik = models.CharField(max_length=128, verbose_name="Yolun Şuanki Durumu")
    Durum = models.BooleanField(verbose_name="Aktif-Pasif Durum")
    sehir = models.ForeignKey(Sehirler)
    ilce = models.ForeignKey(Ilceler)
    slug = models.SlugField(max_length=128, verbose_name="Url")

    def unicode(self): 
        return self.sehir.name
        return self.ilce.name
        return self.NotBaslik
        return self.Tavsiye
        return self.Durum
        return self.DurumGecerlilik
        return self.DurumAciklama
    
    class Meta:
        verbose_name = "Yol Notları"
        verbose_name_plural = "Yol Notları"
    class Admin:
        list_display = ("ilce", "sehir", "Tavsiye", "NotBaslik", "DurumAciklama")
        search_fields = ["ilce", "NotBaslik"]
        list_filter = ("ilce", "NotBaslik")
