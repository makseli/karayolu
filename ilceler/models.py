#*-* coding: utf-8-*-
from django.db import models
from tck.iller.models import Sehir

class Ilce(models.Model):
    ilce_adi = models.CharField(max_length=32, verbose_name="Ilce Adi")
    ilce_tanitim  = models.TextField(verbose_name="Tanitim", blank=True, null=True)
    sehir = models.ForeignKey(Sehir) 
    slug = models.SlugField(max_length=128, verbose_name="Url")
    
    def __unicode__(self):
        return self.ilce_adi
        return self.sehir
 
    class Meta(object):
        verbose_name = "İlçelerimiz"
        verbose_name_plural = "Ilçelerimiz"
    
    class Admin:
        list_display = ("ilce_adi", "sehir", "ilce_tanitim",)
        search_fields = ["ilce_adi", "sehir", "ilce_tanitim"]
        list_filter = ("ilce_adi", "sehir")