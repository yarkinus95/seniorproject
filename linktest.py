from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from time import sleep

#############################################HEPSİBURADA SAYFALARIN İÇLERİYLE ÇALIŞAN VERSİYON

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
liste = []

a = 1
while a<=2:
    r = requests.get("https://www.n11.com/ayakkabi-ve-canta/erkek-ayakkabi?ipg="+str(a)+"",headers=headers)
    soup = BeautifulSoup(r.content,"lxml")
    print("Arama başlatıldı\n")
    sleep(6)
    yeni_fiyat = soup.find("input", attrs={"id": "productPrice"})
    yeni_fiyat


    a=a+1







