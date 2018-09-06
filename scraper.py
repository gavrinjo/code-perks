from bs4 import BeautifulSoup as bs
from requests import get
import re

#keyword = input("Input search keyword ->->->->->")
base_url = f"https://www.moj-posao.net/Pretraga-Poslova/?keyword=vozac&area=2&category="

print("\nsearch results\n")

r = get(base_url)
html_soup = bs(r.text, "html.parser")

# Make sure there are more than one page, otherwise, set to 1.
try:
    num_pages = int(re.findall("\d+$", html_soup.find(class_="last icon").a.get("href"))[0])
except AttributeError:
    num_pages = 1

# Build up a URL list
url_list = ["{}&page={}".format(base_url, str(page)) for page in range(1, num_pages + 1)]

stack = []
company_lst=[]
position_lst=[]
location_lst=[]
deadline_lst=[]
href_lst=[]

for url in url_list:
    rp = get(url)
    soup = bs(rp.text, "html.parser")
    for company in soup.find_all(True, {"class": ["job-position"]}):
        company_lst.append(company.parent.parent.parent.a.img.get("title"))
    for company in soup.find_all(True, {"class": ["job-company"]}):
        company_lst.append(company.text.strip())
    for position in soup.find_all(True, {"class": ["job-position", "job-title"]}):
        position_lst.append(position.text.strip())
    for location in soup.find_all(True, {"class": ["job-location"]}):
        location_lst.append(location.text.strip())
    for deadline in soup.find_all(True, {"datetime": [True]}):
        deadline_lst.append(deadline.text.strip())
    for href in soup.find_all(True, {"class": ["job-position", "job-title"]}):
        if href.parent.get("href") is not None:
          href_lst.append(href.parent.get("href"))
        else:
          href_lst.append(href.a.get("href"))

for a, b, c, d, e in zip(company_lst, position_lst, location_lst, deadline_lst, href_lst):
        stack.append(dict(company=a, position=b, location=c, deadline=d, href=e))

for i in stack:
  print(i)

