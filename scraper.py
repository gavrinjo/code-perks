from bs4 import BeautifulSoup as bs
from requests import get
import re

keyword = input("Input search keyword ->->->->->")
base_url = f"https://www.moj-posao.net/Pretraga-Poslova/?keyword={keyword}&area=2&category="

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

"""
for i in html_soup.find_all(True, {"class": ["job-position"]}):
    print(i.a.get("href"))
"""
# Make dictionary
stack = []
for url in url_list:
    rp = get(url)
    soup = bs(rp.text, "html.parser")
    job_position = soup.find_all(True, {"class": ["job-position", "job-title"]})
    job_location = soup.find_all(True, {"class": ["job-location"]})
    job_deadline = soup.find_all(True, {"datetime": [True]})
    for a, b, c in zip(job_position, job_location, job_deadline):
        stack.append(dict(position=a.text.strip(), location=b.text.strip(), deadline=c.text.strip()))

# print(stack)

for i in stack:
    print(i)
