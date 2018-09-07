from bs4 import BeautifulSoup as bs
from requests import get
import re

#keyword = input("Input search keyword ->->->->->")
base_url = f"https://www.moj-posao.net/Pretraga-Poslova/?keyword=projektant&area=2&category="

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
company_lst = []
position_lst = []
location_lst = []
deadline_lst = []
href_lst = []


# for testing purposis

"""
for company in html_soup.find_all(True, {"class": ["job-position", "job-title"]}):
    if company.get("class")[0] == "job-position":
        try:
            print(company.parent.parent.parent.a.img.get("title"))
        except AttributeError:
            print(company.parent.parent.parent.img.get("title"))
    else:
        print(company.find_next_sibling("p").text.strip())


src = html_soup.find(class_ = "featured")
#for i in stack:
#  print(i)
print(src.prettify())
"""

# work in progress

for url in url_list:
    rp = get(url)
    soup = bs(rp.text, "html.parser")
    for company in html_soup.find_all(True, {"class": ["job-position", "job-title"]}):
        if company.get("class")[0] == "job-position":
            try:
                company_lst.append(company.parent.parent.parent.a.img.get("title"))
            except AttributeError:
                company_lst.append(company.parent.parent.parent.img.get("title"))
        else:
            company_lst.append(company.find_next_sibling("p").text.strip())
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
  print("\n")
  for o in i:
    print(i[o])
