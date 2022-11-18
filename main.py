from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as  np
from openpyxl import workbook

headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
from time import sleep

liste =[]
pages = np.arange(1,10,1)
a=1
while a<8:
    sleep(1)
    url = "https://www.hepsiburada.com/spor-ayakkabilar-c-384551?filtreler=cinsiyet%3AErkek&page="+str(a)
    a=a+1
    get = requests.get(url, headers=headers)
    content = get.content
    soup = BeautifulSoup(content, "html.parser")
    isim = soup.find_all("h3")
    fiyat = soup.find_all(attrs={"data-test-id":"price-current-price"})
    for i  in  isim:
        i=i.text
        liste.append(i)




del liste[0]
print(liste)
df=pd.DataFrame()
df["isim"] =liste[0::1]

df.to_excel("deneme.xlsx",  index=  False)





st1 = soup.find("div", attrs={"class": "productListContent-tEA_8hfkPU5pDSjuFdKG"})
st2 = st1.find("li", attrs={"class": "productListContent-zAP0Y5msy8OHn5z7T_K_"})
