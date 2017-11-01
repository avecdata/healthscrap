import glob
import pandas as pd
import chardet
import codecs
import sys,xlrd
from xlrd import open_workbook
import os.path

var = pd.DataFrame
myvar = pd.DataFrame
rootDir = 'C:/Users/vinicius.dourado.MPT/Dropbox/tabnet/spabr/'
for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
    print('Found directory: %s' % dirName)
    count = 1
    for fname in fileList:
        filepath = os.path.join(rootDir, dirName, fname)
        myvar = pd.read_csv(filepath, sep=";")
        if (count == 1):
            var = myvar
        else:
            var = pd.concat([var, myvar], axis=0)    
        count +=1
        
var = var[~(var['Municipio'].str.contains('Total|&'))]

var["cod_municipio"], var["desc_municipio"] = zip(*var["Municipio"].str.split(' ',1).tolist())
del var['Municipio']
var["cod_municipio"]  = var.cod_municipio.astype(int)

var["mes"], var["ano"] = zip(*var["periodo"].str.split('_',1).tolist())
del var['periodo']

var['Quantidade aprovada'] = var['Quantidade aprovada'].replace(['-'], '0')
var['Valor aprovado'] = var['Valor aprovado'].replace(['-'], '0')
var

var.to_csv('C:/Users/vinicius.dourado.MPT/Dropbox/tabnet/spabr/Dados detalhados das AIH - por local internação - Brasil_2008emdiante.csv',sep=";" , columns=["cod_municipio","desc_municipio","Quantidade aprovada","Valor aprovado","mes","ano"], index=False)


