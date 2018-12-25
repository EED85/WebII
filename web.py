#import modules

import math
import os
import re
import socket
import time

import bs4
import pandas
import requests
from bs4 import BeautifulSoup
import sys 
import os
#define variables

#-------------------------------------------------
#0) Initialisierung
#------------------------------------------------

#import global variables
sys.path.append(os.path.abspath("C:/Users/EricBrahmann/EED-Solutions by Eric Brahmann/Ideal Dental - Dateien Code/webII"))
import vars_module
url_root = = vars_module.vars.def_global_()


#Log
path_code = 'C:/Users/EricBrahmann/EED-Solutions by Eric Brahmann/Ideal Dental - Dateien Code/webII'
outpath = path_code + '/out'
logfile =  outpath+'log.txt'  
localtime = time.asctime( time.localtime(time.time()) )
ip_address = socket.gethostbyname(socket.gethostname())     
with open(logfile,'w') as f:
        f.write('start: ' + localtime)
        f.write('/nip: ' + ip_address) 

# variables


    

    #Excel output
l = [] #temporary list 
d = {} #temporary dictionary
df1='' #Pandas Dataframes

sheet_out = "Tabelle1"

    # Steuervariablen
max_web_i = 2 #maximum loop for webscrapping

    # URLs
url = url_root+'/produkte'

    #Control
cr = 0 #Count of Web requests
TEST = 1
I=0;J=0
#-------------------------------------------------
#1) Start
#------------------------------------------------


if TEST:
    url = 'C:\\Users\\EricBrahmann\\EED-Solutions by Eric Brahmann\\Ideal Dental - Dateien Code\\webII\\in\\000_view-source_https_produkte.html'
    soup = BeautifulSoup(open(url), "html.parser")

else:
    r = requests.get(url);cr = cr+1
    c = ''
    soup = ''

all_cat0 = soup.find_all("div",{"class":"col1 floatleft"})
l = []
I=0
for item in all_cat0:
    I+=1
    print(item.Text)
    sl0 = item.find_all("a")
    print ('found ' +str(len(sl0)) + ' sublinks') 
    J = 0
    for  link in sl0:
        d={}
        has_link = link.has_attr('href')
        print('Hat link',has_link)
        if has_link:
            J+=1
            d["index"] = J
            if TEST:
                d["url"] = link['href'] #put absolute URL in offline file 
            else:
                d["url"] = url_root + link['href']
            d["Kategorie - Level0"] = link.text
            d["Kategorie - Level1"] = ""
            d["Kategorie - Level2"] = ""
                    
            l.append(d)
            print (link.text,link['href'])


print('cat read')

l[0]