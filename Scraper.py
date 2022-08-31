import requests
from bs4 import BeautifulSoup
import csv

class scraping:
  
  def libraries():
      response = requests.get("https://quotes.toscrape.com/")
      soup= BeautifulSoup(response.text,'lxml')
      return soup
       
  def f_open():
      f =open("file1.csv","w")
      return f

  def scrap(self):
    x= scraping.f_open() 
    products=('Quotes','Author','Tags')
    x.write(str(products) + "\n" +"\n")

    quote = []
    z = scraping.libraries()
    
    qs =z.find_all("div",class_='quote')
    for j in qs:
        q = j.find('span',class_='text').text
        ath_name = j.find('small',class_='author').text     
        tag=j.find('div',class_='tags').meta['content']
        quote=[q, ath_name, tag]
    
        x.write(str(quote) +"\n" +"\n")

    x.close() 
s = scraping()
s.scrap()
