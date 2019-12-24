from django.shortcuts import render
import pipi as pd
import numpy as np
import requests 
import datetime

from bs4 import BeautifulSoup as bs
from progressbar import *
from IPython.display import clear_output

#Ana Sayfa view dosyası
def home_view(request):
    #Kategoriler
    categories=["https://www.dunya.com/gundem"]
    links = []
    titles = []
    #Öncelikle bir Kategori seçiyoruz.
    for category in categories:
        #Kategorinin içerisinde sırayla 100 sayfa gezineceğiz.
        for i in range(1,2):
            try:
                #Url'nin içerisindeki bütün html dosyasını indiriyoruz.
                html = requests.get(category).text
                soup = bs(html, "html.parser")
                
                #Yukarıdaki şemadada görüldüğü gibi bütün makaleler bu  element'in içerisinde yer alıyor.
                #Bizde bütün makaleleri buradan tags adında bir değişkene topluyoruz.
                tags = soup.findAll("ul",class_="clearfix")[4]
                #Sırayla bütün makalelere girip, href'in içerisindeki linki urls adlı listemize append ediyoruz.
                for a in tags.find_all('a', href=True):
                    links.append(a['href'])
                for a in tags.find_all('a', href=True):
                    titles.append((a['title']))
            except IndexError:
                break
    context={
        'titles':titles,
        'links':links,
    }
    return render(request,'home.html',context)