def webII_test(url_root='',path=''):
    print(url_root)
    print(path)
    import os


def webII(url_root,path):
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
    logging.Info('0.2) importing modules\n')
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
    #-------------------------------------------------
    #0.3) define variables
    #-------------------------------------------------
    logging.Info('0.3) define variables\n')
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
    max_web_i = 2 #maximum loop for webscrapping
        # URLs
    url = url_root+'/produkte'
        #Control
    cr = 0 #Count of Web requests
    TEST = 1
    I=0;J=0
    #-------------------------------------------------
    #1) Start
    #-------------------------------------------------
    logging.info('\n' + '-'*30 + '\n1) START\n' + '-'*30 + '\n')
    if TEST:
        url = 'C:\\Users\\EricBrahmann\\EED-Solutions by Eric Brahmann\\Ideal Dental - Dateien Code\\webII\\in\\000_view-source_https_produkte.html'
        soup = BeautifulSoup(open(url), "html.parser")
    else:
        r = requests.get(url);cr = cr+1
        logging.debug('REQUEST No ' + str(cr) + ': ' + url )
        c = ''
        soup = ''
    all_cat0 = soup.find_all("div",{"class":"col1 floatleft"})
    l = []
    I=0
    for item in all_cat0:
        I+=1
        print(item.Text)
        sl0 = item.find_all("a")
        logging.debug ('found ' +str(len(sl0)) + ' sublinks') 
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
    T = time.clock()
    RUNTIME = time.strftime("%H:%M:%S", time.gmtime(T-t0))
    logging.info('END \n\n RUNTIME :' + RUNTIME)
