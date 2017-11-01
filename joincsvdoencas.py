import glob
import pandas as pd
import numpy as np
import codecs, shutil
import sys, shutil
import os.path
import unicodedata

rootDir = r'C:\Users\vinicius.dourado.MPT\Dropbox\tabnet\coque'
finalDir = r'C:\Users\vinicius.dourado.MPT\Dropbox\tabnet\doencas sinan'

var = pd.DataFrame

uf = {"11":"RO", "12":"AC", "13":"AM","14":"RR","15":"PA","16":"AP","17":"TO",
        "21":"MA","22":"PI","23":"CE","24":"RN","25":"PB","26":"PE","27":"AL","28":"SE","29":"BA",
        "31":"MG","32":"ES","33":"RJ","35":"SP",
        "41":"PR","42":"SC","43":"RS",
        "50":"MS","51":"MT","52":"GO","53":"DF"
}

regiao = {"1":"Norte", "2":"Nordeste", "3":"Sudeste","4":"Sul","5":"Centro-Oeste"}

for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
    print('Found directory: %s' % dirName)
    count = 0
    total = len(fileList)
    for fname in fileList:
        filepath = os.path.join(rootDir, dirName, fname)
        print(filepath)
        var = pd.read_csv(filepath, sep=";", encoding='latin1')
        notificacao = var.columns[1]
        var = var[~(var[u'Municipio de residencia'].str.contains('Total|&'))]
        var["cod_municipio"], var["desc_municipio"] = zip(*var[u'Municipio de residencia'].str.split(' ',1).tolist())
        del var[u'Municipio de residencia']
        var['uf'] = var['cod_municipio'].str[:2].map(uf)
        var['regiao'] = var['cod_municipio'].str[:1].map(regiao)
        var["cod_municipio"]  = var.cod_municipio.astype(int)
        var["ano"] = var["periodo"]
        var = var.replace(['-'], '0')
        var['doenca'] = var['doenca'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        if (count == 0):
            var.to_csv(finalDir+'\ok.csv',header=True, encoding='utf-8', sep=";" , columns = ['cod_municipio', 'desc_municipio','uf','regiao',notificacao,'ano', u'doenca' ], index=False)
            #shutil.move(filepath, targetDir +"\"+fname)
        else:
            var.to_csv(finalDir+'\ok.csv', mode='a', header=False, encoding='utf-8', sep=";" , columns = ['cod_municipio', 'desc_municipio','uf','regiao',notificacao,'ano', u'doenca' ],  index=False)    
            #shutil.move(filepath, targetDir +'\\'+fname)        
        count +=1
        del var
        print(str(count) +" de "+ str(total))
    








