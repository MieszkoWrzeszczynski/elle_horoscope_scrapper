from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys

url = sys.argv[1]
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

#remove ad
for el in soup.select('div.embed'):
  el.decompose()

horoscope_title = soup.find('h1', attrs={'class': 'content-hed'}).text.strip()
date = soup.find('time', attrs={'class': 'content-info-date'}).text.strip()
authorElement = soup.find('span', attrs={'class': 'byline-name'})
authorString =  authorElement.text.strip() if authorElement else ''

print(horoscope_title, '\n')
print(authorString, '\n')
print(date, '\n')

#content
for item in soup.findAll("p", {"class": "body-text"}):
  print(item.text.strip(), '\n')
