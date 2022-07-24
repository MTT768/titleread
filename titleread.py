import os
import sys

ilkkonum = os.getcwd() #Dosya Açıldığı İlk Zamanki Konum Değişkene Kaydediliyor

def title(url):
    import requests
    from bs4 import BeautifulSoup
    rsite = requests.get(url)
    bsdzn = BeautifulSoup(rsite.content,"lxml")
    print(str(bsdzn.title).replace('<title>','').replace('</title>',''))

def modul_kur(): #Modül Kurma Fonksiyonu
    os.system('py -3 -m pip install BeautifulSoup4 >nul')
    os.system('py -3 -m pip install requests >nul')
    os.chdir(f'{ilkkonum}')

if os.name != "nt":
    sys.exit()
os.chdir(f'C:\\Users\\{os.getlogin()}\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages')
if 'bs4' not in os.listdir():
    modul_kur()
if 'requests' not in os.listdir():
    modul_kur()