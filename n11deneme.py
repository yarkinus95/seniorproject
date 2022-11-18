from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

#############################################HEPSİBURADA SAYFALARIN İÇLERİYLE ÇALIŞAN VERSİYON

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

liste = []

a = 1
while a<=1:
    r = requests.get("https://www.n11.com/ayakkabi-ve-canta/erkek-ayakkabi?ipg="+str(a)+"",headers=headers)
    soup = BeautifulSoup(r.content,"lxml")
    print("Arama başlatıldı\n")
    st1 = soup.find("div", attrs={"class": "productArea"})
    # print("ilk class bulundu\n",st1)
    st2 = st1.find_all("li", attrs={"class": "column"})







    for detaylar in st2:
        link = detaylar.a.get("href")

        print("ürün linki",link)

        r1 = requests.get(link,headers=headers)
        soup1 = BeautifulSoup(r1.content,"lxml")

        yeni_fiyat = soup1.find("input",attrs={"id":"productPrice"})
        #print(yeni_fiyat)

        #print(indirim)
        try:
            puan = soup1.find("strong",attrs={"class":"ratingScore r90"})
        except:
            puan = "puan yok"
        #print(puan)
        değerlendirme = soup1.find("span",attrs={"class":"reviewNum"})
        #print(değerlendirme)
        ürün_adı = soup1.find("h1",attrs={"class":"proName"}).text.strip()
        print(ürün_adı)





        liste.append([ürün_adı,link,yeni_fiyat,puan,değerlendirme])
        print("ürün listeye eklendi!\n")
        print(liste)

    a = a+1
df = pd.DataFrame(liste)
df.columns=["ürün_adı","link","yeni_fiyat","puan","değerlendirme_sayısı"]
df.to_excel("ayakkabı_3.xlsx")