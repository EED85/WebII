# def webII(url_root,path,TEST=1):
import os
#-------------------------------------------------
#0) Initialisierung
#-------------------------------------------------
os.chdir(path)
os.getcwd()
logfile =  'out/webII.log'
open(logfile, 'w').close() #reset log file
# CRITICAL 50
# ERROR 40
# WARNING 30
# INFO 20
# DEBUG 10
# NOTSET 0
import logging
    #set logging to txtfile
logging.basicConfig(filename=logfile,level=logging.DEBUG,format='%(asctime)s - %(levelname)s %(message)s')
    #set logging to console
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
console.setFormatter(formatter)
logging.getLogger("").addHandler(console)
logging.info('\n' + '-'*30 + '\n0) Initialisierung\n' + '-'*30 + '\n')
    #-------------------------------------------------
    #0.2) Modules
    #-------------------------------------------------
logging.info('0.2) importing modules\n')
import sys 
import pkg_resources
import time
import math
import numpy as np
import pandas as pd
import re
import socket
import bs4
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
#-------------------------------------------------
#0.3) define variables
#-------------------------------------------------
logging.info('0.3) define variables\n')
logging.info(url_root)
ip_address = socket.gethostbyname(socket.gethostname())
logging.info('IP: ' + ip_address + '\n')
t0 = time.clock();T=0;RUNTIME = time.strftime("%H:%M:%S", time.gmtime(0))
logging.info('PACKAGE VERSION\n')
for d in pkg_resources.working_set:
    logging.debug(d.project_name + " - " + d.version)
# variables
    #Excel output
l = [] #temporary list 
d = {} #temporary dictionary
df1='' #Pandas Dataframes
sheet_out = "Tabelle1"
    # Steuervariablen
max_web_i = 2  #maximum loop for webscrapping 
# max_web_i = float('Inf') # scrap all

    # URLs
url = url_root+'/produkte'
    #Control
cr = 0 #Count of Web requests

load_df = [True #cat0
        ,False #cat1
        ]
logging.info('load_df = ' + str(load_df))
I=0;J=0
#-------------------------------------------------
#1) Start
#-------------------------------------------------
logging.info('\n' + '-'*30 + '\n1) START\n' + '-'*30 + '\n')


logging.info('\n' + '-'*30 + '\n1.1) Cat0\n' + '-'*30 + '\n')
cat_label = 'Kategorie_0'
file = r'out' + '\\' + cat_label

if load_df[0]:
    df1 = pd.read_pickle(file + '.pkl')
else:
    if TEST:
        url = r'\in\000_view-source_https_produkte.html'
        soup = BeautifulSoup(open(url), "html.parser")
        logging.info('TEST')
    else:
        r = requests.get(url);cr = cr+1
        r
        logging.debug('REQUEST No ' + str(cr) + ': ' + url )
        c = r.content
        soup = BeautifulSoup(c,"html.parser")

    all_cat0 = soup.find_all("a",{"class":"trail"})
    logging.info('Found Catagories -  ' + str(len(all_cat0)))

    l = []
    I=0

    
    for item in all_cat0:
        has_link = item.has_attr('href')
        if has_link:
            d={}
            I+=1
            logging.debug('I=' + str(I) + ' - ' + item.text + ' - ' + item['href'])
            d["index"] = I
            if TEST:
                d["url"] = item['href'] #put absolute URL in offline file 
            else:
                d["url"] = url_root + item['href']
                d["Kategorie - Level0"] = item.text
                d["Kategorie - Level1"] = ""
                d["Kategorie - Level2"] = ""
                l.append(d)
    df1 = DataFrame(l)
    logging.info(df1.head())
    df1.to_csv( file + '.csv') 
    df1.to_pickle(file + '.pkl')


logging.info('\n' + '-'*30 + '\n1.2) Cat1\n' + '-'*30 + '\n')

l[0]
T = time.clock()
RUNTIME = time.strftime("%H:%M:%S", time.gmtime(T-t0))
logging.info('END \n\n RUNTIME :' + RUNTIME)



# def webII_test(url_root='',path='',TEST=1):
#     print(url_root)
#     print(path)
#     print(TEST)
#     print('modified')

# print("END")
