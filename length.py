import csv
import requests
from bs4 import BeautifulSoup
import re 


url = ('https://www.ntia.doc.gov/grants-combined?page=%d')

data = []

for x in range(0, 16):
   url = ('https://www.ntia.doc.gov/grants-combined?page=%d' % (x))
   #print('https://www.ntia.doc.gov/grants-combined?page=%d' % (x))

   response = requests.get(url)
   html = response.content

   soup = BeautifulSoup(html, 'lxml')

   grants = soup.findAll("div", class_="ntia_content_title")
    
   len(grants)
   
   data.extend(grants)
   print()

   titles = soup.findAll("div", class_="ntia_content_title")
   for grant in grants: 
      print(grant.next.contents[0])
len(data)
