#! /usr/bin/python
# -*- coding: ISO-8859-1 -*-

import glob
import pandas as pd
import chardet
import codecs
import sys,xlrd
from xlrd import open_workbook
import os.path

class Nibr:
	__gui = None

def __init__(self, gui):  
    self.__gui = gui  	

def agregacaodoscsv_nibr():
    var = pd.DataFrame
    myvar = pd.DataFrame
    rootDir = 'C:/Users/vinicius.dourado.MPT/Dropbox/tabnet/nibr/'
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

    var['Internacoes'] = var['Internacoes'].replace(['-','...'], '0')
    var['AIH aprovadas'] = var['AIH aprovadas'].replace(['-','...'], '0')
    var['Valor total'] = var['Valor total'].replace(['-','...'], '0')
    var['Valor servicos hospitalares'] = var['Valor servicos hospitalares'].replace(['-','...'], '0')
    var['Val serv hosp - compl federal'] = var['Val serv hosp - compl federal'].replace(['-','...'], '0')
    var['Val serv hosp - compl gestor'] = var['Val serv hosp - compl gestor'].replace(['-','...'], '0')
    var['Valor servicos profissionais'] = var['Valor servicos profissionais'].replace(['-...'], '0')
    var['Val serv prof - compl federal'] = var['Val serv prof - compl federal'].replace(['-','...'], '0')
    var['Val serv prof - compl gestor'] = var['Val serv prof - compl gestor'].replace(['-','...'], '0')
    var['Valor medio AIH'] = var['Valor medio AIH'].replace(['-','...'], '0')
    var['Valor medio intern'] = var['Valor medio intern'].replace(['-','...'], '0')
    var['Dias permanencia'] = var['Dias permanencia'].replace(['-','...'], '0')
    var['Media permanencia'] = var['Media permanencia'].replace(['-','...'], '0')
    var['Obitos'] = var['Obitos'].replace(['-','...'], '0')

    var.columns



    var.to_csv('C:/Users/vinicius.dourado.MPT/Dropbox/tabnet/nibr/Morbidade Hospitalar do SUS - por local de internação - Brasil2008emdiante.csv',sep=";" , columns=["cod_municipio", "desc_municipio","Internacoes", "AIH aprovadas", "Valor total","Valor servicos hospitalares", "Val serv hosp - compl federal",
    "Val serv hosp - compl gestor", "Valor servicos profissionais", "Val serv prof - compl federal", "Val serv prof - compl gestor", "Valor medio AIH", 
    "Valor medio intern", "Dias permanencia", "Media permanencia", "Obitos", "mes",  "ano"], index=False)



