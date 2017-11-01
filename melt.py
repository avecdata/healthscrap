import glob
import pandas as pd
import numpy as np
import codecs, shutil
import sys, shutil
import os.path

rootDir = r'C:\Users\vinicius.dourado.MPT\dropbox_avec\Dropbox\AVEC\Conteúdo\Material para classificação\Agronegócios\Safra\csv'
targetDir = u'C:/Users/vinicius.dourado.MPT/dropbox_avec/Dropbox/AVEC/Conteúdo/Material para classificação/Agronegócios/Safra/csv'


var = pd.DataFrame

for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
    print('Found directory: %s' % dirName)
    count = 0
    total = len(fileList)
    for fname in fileList:
        filepath = os.path.join(rootDir, dirName, fname)
        var = pd.read_csv(filepath, sep=",", encoding='latin1')
        print(fname)


var2 = pd.melt(var, id_vars=["tipo"], 
                  var_name="periodo", value_name="valor")

var2 = var2.sort_values(by=["tipo","periodo"])

var2.to_csv(targetDir+'/final.csv', mode='a', header=True, encoding='latin1', sep="," ,  index=False)    



import datetime

df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 6,
            'B': ['A', 'B', 'C'] * 8,
            'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 4,
            'D': np.random.randn(24),
            'E': np.random.randn(24),
            'F': [datetime.datetime(2013, i, 1) for i in range(1, 13)] +
            [datetime.datetime(2013, i, 15) for i in range(1, 13)]})

df

var3 = pd.pivot_table(var2, index=['periodo'], columns=['tipo'])

var3.index = var3.index.str.slice(0,5)

var3.index

var3.to_csv(targetDir+'/final.csv', mode='a', header=True, encoding='latin1', sep="," )   






















