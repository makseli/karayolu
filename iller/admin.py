#*-* coding: utf-8-*-
from django.contrib import admin
from tck.iller.models import Sehirler,Ilceler,YolNotlari

class SehirlerAdmin(admin.ModelAdmin):
    ordering = ['-sehir']
    list_display = ('sehir','il_tck_web')
    list_filter = ('sehir','il_tck_web')
    search_fields = ['sehir','il_tck_web']
    prepopulated_fields = {'slug':('sehir',)}
    
def sehirler(self):
    s = Sehirler.objects.filter(sehir=self)
    return len(s)
sehirler.short_description = 'Sehirler'

class Meta:
    verbose_name = 'Şehirler'
    verbose_name_plural = "Şehirlerimiz"
    
    
    
    

class IlcelerAdmin(admin.ModelAdmin):
    ordering = ['ilce_adi', 'sehir',]
    list_display = ('ilce_adi','sehir')
    list_filter = ('ilce_adi','sehir')
    search_fields = ['ilce_adi', 'sehir']
    prepopulated_fields = {'slug':('ilce_adi',)}

def ilceler(self):
    i = Ilceler.objects.filter( ilce_adi=self)
    return len(i)
ilceler.short_description = 'İlçeleri'

class Meta(object):
    verbose_name = 'İlçeler'
    verbose_name_plural = "Ilçelerimiz"
    
    
    
    
    
    
class YolNotlariAdmin(admin.ModelAdmin):
    ordering = ['NotBaslik','ilce', 'sehir']
    list_display = ('NotBaslik','sehir','ilce','DurumGecerlilik')
    list_filter = ('NotBaslik','DurumGecerlilik', 'sehir')
    search_fields = ['NotBaslik', 'sehir']
    prepopulated_fields = {'slug':('NotBaslik',)}

def yolnotlari(self):
    e = YolNotlari.objects.filter(NotBaslik=self)
    return len(e)
yolnotlari.short_description = 'Yol Notları'

class Meta(object):
    verbose_name = 'Yol Notları'
    verbose_name_plural = "Yol Notları"
    

list_display = ('sehir','il_tck_web',sehirler)
list_display = ('ilce_adi', 'sehir',ilceler)
list_display = ('NotBaslik','ilce', 'sehir','DurumGecerlilik',yolnotlari)

admin.site.register(YolNotlari, YolNotlariAdmin)
admin.site.register(Sehirler, SehirlerAdmin)
admin.site.register(Ilceler, IlcelerAdmin)