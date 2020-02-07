from bs4 import BeautifulSoup as bs
from requests import get
import re

url = "https://www.njuskalo.hr/prodaja-stanova/zagreb?price%5Bmin%5D=5000&price%5Bmax%5D=133000&includeOtherCategories=1&livingArea%5Bmin%5D=70&adsWithImages=1&flatBuildingType=flat-in-residential-building&balconyInfo=allthree&buildingFloorPosition%5Bmin%5D=1&page=1"

raw_data = get(url)
soup_data = bs(raw_data.text, 'html.parser')

#soup_data = soup_data.prettify()

for article in soup_data.find_all('article'):
  print()
  print(article.h3.a.get_text())
  print(article.get(calss="entity-description-main"))

