#import modules

import requests
import bs4
from bs4 import BeautifulSoup
import pandas
import os
import re
import time
import math
import socket


#define variables

#-------------------------------------------------
#0) Initialisierung
#------------------------------------------------

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


    #Pandas Dataframes
df1=''

    #Excel output

sheet_out = "Tabelle1"

    # Steuervariablen
max_web_i = 2 #maximum loop for webscrapping

    # URLs
url = url_root

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

for item in all_cat0:
    I+=1
    print(item.Text)
    sl0 = item.find_all("a")
    print ('found ' +str(len(sl0)) + ' sublinks') 
    J = 0
    for  l0 in sl0:
        
        has_link = l0.has_attr('href')
        print('Hat link',has_link)
        if has_link:
            J+=1
            print (l0.text,l0['href'])

print('cat read')

  
    

