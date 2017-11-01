import urllib, bs4, pandas, locale
from bs4 import BeautifulSoup
import lxml
# -*- coding: cp1252 -*-

soup = BeautifulSoup(urllib.request.urlopen("http://tabnet.datasus.gov.br/cgi/deftohtm.exe?sih/cnv/qrbr.def").read(),"lxml");

def_value = []
for w in soup.find_all('select'):
    if not w.attrs['name'].startswith('lista'):
        def_value.append(w.attrs['name'])
    #print(w.attrs['name'])

def_value_v = []
for item in soup.find_all('option',attrs={'selected':True}):
    def_value_v.append(item.attrs['value'])
    #print(''.join(str(item.find(text=True))));

def_value_v

par = ''
count = 0
for word in def_value:
    par = par + word +'='+ def_value_v[count]+'&'
    count += 1
par = par + 'zeradas=exibirlz&formato=prn&mostre=Mostra'

d = {u'à' : '%e0',u'á' : '%e1',u'â' : '%e2',u'ã' : '%e3',u'ä' : '%e4',u'å' : '%e5',u'æ' : '%e6',u'ç' : '%e7',u'è' : '%e8',u'é' : '%e9',u'ê' : '%ea',
u'ë' : '%eb',u'ì' : '%ec',u'í' : '%ed',u'î' : '%ee',u'ï' : '%ef'}

    

    
