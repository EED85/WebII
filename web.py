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
l_df = [] #list of Pandas Dataframes
for I in range(3):
    df_tmp = DataFrame([])
    l_df.append(df_tmp)


sheet_out = "Tabelle1"
    # Steuervariablen
max_web_i = [float('Inf') #cat0 -> is not used
            ,float('Inf') #cat1
            ,float('Inf') #cat2
            ]  #maximum loop for webscrapping 
# max_web_i = float('Inf') # scrap all

    # URLs
url = url_root+'/produkte'
    #Control
cr = 0 #Count of Web requests
load_df = [True #cat0
        ,True #cat1
        ,False #cat2
        ]
logging.info('load_df = ' + str(load_df))
I=0;J=0
#-------------------------------------------------
#1) Start
#-------------------------------------------------
logging.info('\n' + '-'*30 + '\n1) START\n' + '-'*30 + '\n')

#-------------------------------------------------
#1.1) Cat0
#-------------------------------------------------
level = 0
logging.info('\n' + '-'*30 + '\n1.' +str(level) + ') Cat1\n' + '-'*30 + '\n')
cat_label = 'Kategorie_0'
file = r'out' + '\\' + cat_label

if load_df[level]:
    df = pd.read_pickle(file + '.pkl')
    logging.info('df was loaded from disk')
    logging.debug(df.head())
    l_df[level] = df
else:
    if TEST:
        url = r'\in\000_view-source_https_produkte.html'
        soup = BeautifulSoup(open(url), "html.parser")
        logging.info('TEST')
    else:
        r = requests.get(url);cr = cr+1
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
    df = DataFrame(l)
    logging.info(df.head())
    df.to_csv( file + '.csv') 
    df.to_pickle(file + '.pkl')
    l_df[level] = df

#-------------------------------------------------
#1.2) Cat1
#-------------------------------------------------
level = 1
logging.info('\n' + '-'*30 + '\n1.' +str(level) + ') Cat1\n' + '-'*30 + '\n')
df1 = l_df[level-1]
cat_label = 'Kategorie_{}'.format(level)
file = r'out' + '\\' + cat_label

if load_df[level]:
    df = pd.read_pickle(file + '.pkl')
    logging.info('df was loaded from disk')
    logging.debug(df.head())
    l_df[level] = df
else:
    I = 0;l=[]
    for index,row in df1.iterrows():
        url = row["url"]
        r = requests.get(url);cr = cr+1
        logging.debug('REQUEST No ' + str(cr) + ': ' + url )
        c = r.content
        soup = BeautifulSoup(c,"html.parser")
        all_cat1 = soup.find("aside",{"class":"sidemenu categories syncheight"})
        sublinks = all_cat1.find_all('li',class_="")
        for link in sublinks:
            link_a = link.find('a')
            has_link = link_a.has_attr('href')
            if has_link:
                d={}
                I+=1
                logging.debug('I=' + str(I) + ' - ' + link_a.text + ' - ' + link_a['href'])
                d["index"] = I
                if TEST:
                    d["url"] = link_a['href'] #put absolute URL in offline file 
                else:
                    d["url"] = url_root + link_a['href']
                    d["Kategorie - Level0"] = row["Kategorie - Level0"]
                    d["Kategorie - Level1"] = link_a.text
                    d["Kategorie - Level2"] = ""
                    l.append(d)
        if index >= max_web_i[level]-1:
            logging.warning('Maximum number of webscapping : {}'.format(max_web_i))
            break
    df = DataFrame(l)
    logging.info(df.head())
    df.to_csv( file + '.csv') 
    df.to_pickle(file + '.pkl')
    l_df[level] = df

#-------------------------------------------------
#1.2) Cat2
#-------------------------------------------------
level = 2
logging.info('\n' + '-'*30 + '\n1.' +str(level) + ') Cat1\n' + '-'*30 + '\n')
df1 = l_df[level-1]

t2 = time.clock()
cat_label = 'Kategorie_{}'.format(level)
file = r'out' + '\\' + cat_label

if load_df[level]:
    df = pd.read_pickle(file + '.pkl')
    logging.info('df was loaded from disk')
    logging.debug(df.head())
    l_df[level] = df
else:
    I = 0;l=[]
    for index,row in df1.iterrows():
        url = row["url"]
        r = requests.get(url);cr = cr+1
        logging.debug('REQUEST No ' + str(cr) + ': ' + url )
        c = r.content
        soup = BeautifulSoup(c,"html.parser")
        #get active subcat
        
        active_subcat = soup.find('span',{'class':'subcategory-activ'})
        active_subcat_text = "" if active_subcat is None else active_subcat.text
        if active_subcat_text == row["Kategorie - Level1"]:
            d={};I+=1
            logging.debug(row["Kategorie - Level1"] + ' has no subcats')
            d["url"] = row["url"]
            d["Kategorie - Level0"] = row["Kategorie - Level0"]
            d["Kategorie - Level1"] = row["Kategorie - Level1"]
            d["Kategorie - Level2"] = row["Kategorie - Level1"]
            #d["index"] = I
            l.append(d)
        else:
            all_cat1 = soup.find("aside",{"class":"sidemenu categories syncheight"})
            sublinks = all_cat1.find_all('li',class_="")
            for link in sublinks:
                link_a = link.find('a')
                has_link = link_a.has_attr('href')
                if has_link:
                    d={}; I+=1
                    logging.debug('I=' + str(I) + ' - ' + link_a.text + ' - ' + link_a['href'])
                    d["index"] = I
                    if TEST:
                        d["url"] = link_a['href'] #put absolute URL in offline file 
                    else:
                        d["url"] = url_root + link_a['href']
                        d["Kategorie - Level0"] = row["Kategorie - Level0"]
                        d["Kategorie - Level1"] = row["Kategorie - Level1"]
                        d["Kategorie - Level2"] = link_a.text
                        l.append(d)
        if index >= max_web_i[level]-1:
            logging.warning('Maximum number of webscapping : {}'.format(max_web_i))
            break
    df = DataFrame(l)
    logging.info(df.head())
    df.to_csv( file + '.csv') 
    df.to_pickle(file + '.pkl')
    l_df[level] = df



T2 = time.clock()
RUNTIME2 = time.strftime("%H:%M:%S", time.gmtime(T2-t2))
logging.info('\n\n RUNTIME - Level {}: '.format(level) + RUNTIME2)




T = time.clock()
RUNTIME = time.strftime("%H:%M:%S", time.gmtime(T-t0))
logging.info('END \n\n RUNTIME :' + RUNTIME)



# def webII_test(url_root='',path='',TEST=1):
#     print(url_root)
#     print(path)
#     print(TEST)
#     print('modified')

# print("END")
