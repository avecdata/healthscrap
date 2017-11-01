import glob
import pandas as pd
import numpy as np
import codecs, shutil
import sys, shutil
import os.path

rootDir = 'C:\Users\Vinicius\Desktop\morbidade_capitulo\extracted'
targetDir = 'C:\Users\Vinicius\Desktop\morbidade_capitulo\transformed'
finalDir = 'd:\ok'

var = pd.DataFrame

for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
    print('Found directory: %s' % dirName)
    count = 0
    total = len(fileList)
    for fname in fileList:
        filepath = os.path.join(rootDir, dirName, fname)
        try:
            var = pd.read_csv(filepath, sep=";", encoding='latin1')
            print(fname)
            var = var[~(var['Municipio'].str.contains('Total|&'))]
            var["cod_municipio"], var["desc_municipio"] = zip(*var["Municipio"].str.split(' ',1).tolist())
            del var['Municipio']
            var["cod_municipio"]  = var.cod_municipio.astype(int)
            var["mes"], var["ano"] = zip(*var["periodo"].str.split('_',1).tolist())
            del var['periodo']
            var = var.replace(['-'], '0')
            if (count == 0):
                var.to_csv(finalDir+'\final.csv',header=True, encoding='latin1', sep=";" , columns = ['cod_municipio', 'desc_municipio', u'Internacoes', u'AIH aprovadas', u'Valor total', u'Valor servicos hospitalares', u'Val serv hosp - compl federal', u'Val serv hosp - compl gestor', u'Valor servicos profissionais', u'Val serv prof - compl federal', u'Val serv prof - compl gestor', u'Valor medio AIH', u'Valor medio intern', u'Dias permanencia', u'Media permanencia', u'Obitos', 'mes', 'ano', u'SCap\xedtulo_CID-10' ], index=False)
                #shutil.move(filepath, targetDir +"\"+fname)
            else:
                var.to_csv(finalDir+'\final.csv', mode='a', header=False, encoding='latin1', sep=";" , columns = ['cod_municipio', 'desc_municipio', u'Internacoes', u'AIH aprovadas', u'Valor total', u'Valor servicos hospitalares', u'Val serv hosp - compl federal', u'Val serv hosp - compl gestor', u'Valor servicos profissionais', u'Val serv prof - compl federal', u'Val serv prof - compl gestor', u'Valor medio AIH', u'Valor medio intern', u'Dias permanencia', u'Media permanencia', u'Obitos', 'mes', 'ano', u'SCap\xedtulo_CID-10' ],  index=False)    
                #shutil.move(filepath, targetDir +'\\'+fname)        
            count +=1
            del var
            
            print(str(count) +" de "+ str(total))
        except Exception, e:
             continue
       
       
       

































