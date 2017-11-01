import simpledbf
from simpledbf import Dbf5

import glob
import pandas as pd
import chardet
import codecs
import sys,xlrd
from xlrd import open_workbook
import os.path

'''
dbf = Dbf5('fake_file_name.dbf')

In : for df in dbf.to_dataframe(chunksize=10000)
....     do_cool_stuff(df)
# Here a generator is returned
'''

class agregaDBF(object):
    
    def __init__(self, sourceDir,targetDir):
        self.sourceDir = sourceDir
        self.targetDir = targetDir
        
    def agregaDBF(self):
        df0 = pd.DataFrame
        df1 = pd.DataFrame
        rootDir = self.sourceDir
        for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
            count = 1
            for fname in fileList:
                if fname.endswith('.dbf'):
                    filepath = os.path.join(rootDir, dirName, fname)
                    dbf1 = Dbf5(filepath, codec='latin1')
                    df0 = dbf1.to_dataframe()
                    if (count == 1):
                        df1 = df0
                    else:
                        df1 = pd.concat([df1, df0], axis=0)    
                    count +=1
        return df1.to_csv(self.targetDir+'agregado.csv',sep=";" , index=False)







