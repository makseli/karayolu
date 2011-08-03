#*-* coding: utf-8-*-
from django.template import Context, loader
from django.http import HttpResponse
from tck.iller.models import Sehir
from tck.ilceler.models import Ilce
from tck.yolnotlar.models import YolNotu

def iller(request):
    iller = Sehir.objects.all().order_by('-id')[:5]
    t = loader.get_template('iller.html') 
    c = Context({ 'iller' : iller },)
    
    return HttpResponse(t.render(c),)

def ilceler(request,slug):
    ilceler = Ilce.objects.all().order_by('-id')[:5]
    t1 = loader.get_template('ilceler.html') 
    c1 = Context({ 'ilceler' : ilceler },)
    
    return HttpResponse(t1.render(c1),)



def yolnotlar(request,slug):
    notlar = YolNotu.objects.all().order_by('-id')[:5]
    t2 = loader.get_template('notlar.html') 
    c2 = Context({ 'notlar' : notlar },)
    
    return HttpResponse(t2.render(c2),)
