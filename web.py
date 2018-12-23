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
#-------------------------------------------------
#1) Start
#------------------------------------------------

r = requests.get(url);cr = cr+1

