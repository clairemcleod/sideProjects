#this parses .html files containing the marathon results data, and writes it to #fullResults.csv via beautifulsoup.

from bs4 import BeautifulSoup
import csv
import glob
import os

def simplify_td(tr, position): #returns string with data of interest
    r1=tr.contents[position].contents
    
# some of the name tr's have an <img> tag as the first content element (index=0)
# for these, the name is actually in the second position (index=1)
# to handle this:    
    
    if position == 1 and len(r1)>1:   
        r2=r1[1]
    elif len(r1):
        r2=r1[0]
    else:
        r2=""
    return r2

headers=['bib', 'name', 'sex', 'age', 'location', 'net', 'clock', 'pace', 'event']
         
with open("fullResults.csv", 'wb') as outputfile:         
    f = csv.writer(outputfile, delimiter=',')
    f.writerow(headers)
    
    for file in glob.glob("*.html"):
        print(file)
    
        soup = BeautifulSoup (open(file))
    
        soup1=soup.tbody
        soup2=soup1.find_next('tbody')
        soup3=soup2.find_all('tr')
    
        for item in soup3:
            bib=simplify_td(item,0)
            name=simplify_td(item,1)
            sex=simplify_td(item,2)
            age=simplify_td(item,3)
            location=simplify_td(item,4)
            net=simplify_td(item,5)
            clock=simplify_td(item,6)
            pace=simplify_td(item,7)
            event=simplify_td(item,8)
            f.writerow([bib, name, sex, age, location, net, clock, pace, event])        
            
    outputfile.flush()    