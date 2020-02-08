import bs4 as bs 
import pandas as pd
import requests as rq
import re


print("Developed By Muhammad Rizwan")
print("Phone: +92 3072946462")
print("Email: allgame45@hotmail.com, admin@rizwan3d.com")
print("website: www.rizwan3d.com")
input("Press Enter to continue...")

pName=[] 
pLink=[] 
pAuth=[] 
pCiteBby=[] 
pAffiliations=[] 
pDOIandDare = []
pPubhistory = []
pKeywords = []
for num in range(1,17787): 
    base_url = 'https://www.mdpi.com/search?q=&journal=sensors&sort=pubdate&page_count=10&view=abstract&year_from=2015&year_to=2020&page_no=' + str(num)
    print("Processing: " + base_url)
    r = rq.get(base_url)
    content = r.text;
    soup = bs.BeautifulSoup(content,'html.parser')
    for a in soup.findAll('div', attrs={'class':'article-content'}):
        print("----------------------------------------------")
        tile =a.find('a', href=True, text=True ,attrs={'class':'title-link'})
        if tile is None:
           continue;
        link = tile['href'];
        pLink.append("https://www.mdpi.com" + link);
        print(link)
        name = tile.getText()
        auDiv =  a.find('div', attrs={'class':'authors'})
        citedby =  a.find('a', attrs={'href':link + '#citedby' })
        if citedby is not None:            
            print(citedby.getText()[9:])
            pCiteBby.append(citedby.getText()[9:])
        else:
            print('0')
            pCiteBby.append('0')
                        
        pName.append(name)
        print(name)
        c = ''
        for spans in a.findAll('span',attrs={'class':'inlineblock'}):
            if "span" in str(spans): 
                print('\t', end = '')  
                c = c + "," + spans.find('a').getText()
                print(spans.find('a').getText())
                
        print(c[1:])
        pAuth.append(c[1:])
        affiliations = a.find('div',attrs={'class': 'affiliations'})
        print(affiliations.getText())
        pAffiliations.append(affiliations.getText())
        data = a.find('div', attrs={'class': 'color-grey-dark'})
        print(data.getText())
        pDOIandDare.append(data.getText())

        _url = "https://www.mdpi.com" + link
        _r = rq.get(_url)
        _content = _r.text;
        _soup = bs.BeautifulSoup(_content,'html.parser')
        pupHis =  _soup.find('div', attrs={'class':'pubhistory'}).getText()
        print(pupHis)
        pPubhistory.append(pupHis)

        Keywords =  _soup.find('span', attrs={'itemprop':'keywords'}).getText()
        print(Keywords)
        pKeywords.append(Keywords)    

df = pd.DataFrame({'Title':pName,'Authors':pAuth,'Affiliations':pAffiliations,'DOI and Date':pDOIandDare,'Cite By' :pCiteBby,'Link:': pLink,'Pub History': pPubhistory,'Keywords': pKeywords}) 
df.to_csv('data.csv', index=False, encoding='utf-8')