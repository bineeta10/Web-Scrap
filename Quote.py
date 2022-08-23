import requests
from bs4 import BeautifulSoup
from csv import writer



with open("New.csv",'w') as csvfile:
    thewriter= writer(csvfile)
    header=['Quotes','Author','Tags']
    thewriter.writerow(header)
    Scrap = []
    website_url = "https://quotes.toscrape.com/"
    res = requests.get(website_url)
    soup = BeautifulSoup(res.text,'lxml')
    
    qs=soup.find_all("div",class_='quote')
    for j in qs:
        quotes=j.find('span',class_='text').text
        #print(f'Quote:{quotes}') 
        ath_name = j.find('small',class_='author').text     
        #print(f'Author_name:{ath_name}')
        tag=j.find('div',class_='tags').meta['content']
        #print(f'Tags:{tag}')
        scrap =[quotes,ath_name,tag]
        thewriter.writerow(scrap)
            
      