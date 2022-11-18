from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

#############################################HEPSİBURADA SAYFALARIN İÇLERİYLE ÇALIŞAN VERSİYON

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

liste = []

a = 1
while a<=4:
    r = requests.get("https://www.hepsiburada.com/spor-ayakkabilar-c-384551?filtreler=cinsiyet%3AErkek&sayfa="+str(a)+"",headers=headers)
    soup = BeautifulSoup(r.content,"lxml")
    print("Arama başlatıldı\n")

    st1 = soup.find("div", attrs={"class": "productListContent-tEA_8hfkPU5pDSjuFdKG"})
    print("ilk class bulundu\n")
    st2 = st1.find_all("li", attrs={"class": "productListContent-zAP0Y5msy8OHn5z7T_K_"})
    print("ikinci class bulundu \n")





    for detaylar in st2:
        link_sonu = detaylar.a.get("href")
        link_bası = "https://www.hepsiburada.com"
        link = link_bası+link_sonu
        print("ürün linki",link)

        r1 = requests.get(link,headers=headers)
        soup1 = BeautifulSoup(r1.content,"lxml")

        yeni_fiyat = soup1.find("span",attrs={"id":"offering-price"}).text.strip().replace("\n","")
        #print(yeni_fiyat)

        indirim = soup1.find("span",attrs={"id":"product-discount-rate"}).text.strip().replace("\n","").replace("\r","")
        #print(indirim)
        try:
            puan = soup1.find("span",attrs={"class":"rating-star"}).text.strip()
        except:
            puan = "puan yok"
        #print(puan)
        değerlendirme = soup1.find("div",attrs={"id":"comments-container"}).text.strip()
        #print(değerlendirme)
        ürün_adı = soup1.find("h1",attrs={"itemprop":"name"}).text.strip()
        #print(ürün_adı)





        liste.append([ürün_adı,link,yeni_fiyat,indirim,puan,değerlendirme])
        print("ürün listeye eklendi!\n")

    a = a+1
df = pd.DataFrame(liste)
df.columns=["ürün_adı","link","yeni_fiyat","indirim_oranı","puan","değerlendirme_sayısı"]
df.to_excel("ayakkabı_3.xlsx")