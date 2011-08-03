#*-* coding: utf-8-*-
from django.db import models
from tck.iller.models import Sehir
from tck.ilceler.models import Ilce

class YolNotu(models.Model):
    NotBaslik = models.CharField(max_length=32, verbose_name="Yol Durum Başlığı")
    DurumAciklama  = models.TextField(verbose_name="Yol Durumu Açıklama", blank=True, null=True)
    Tavsiye  = models.TextField(verbose_name="Durum için Tavsiye", blank=True, null=True)
    MapLokeysin = models.TextField(max_length=128, verbose_name="Yol Google Map Koordinatları", blank=True, null=True)
    DurumGecerlilik = models.CharField(max_length=128, verbose_name="Yolun Şuanki Durumu", blank=True, null=True)
    Durum = models.BooleanField(verbose_name="Aktif-Pasif Durum")
    sehir = models.ForeignKey(Sehir)
    ilce = models.ForeignKey(Ilce)
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