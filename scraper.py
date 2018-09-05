from bs4 import BeautifulSoup
from requests import get
import re

keyword = input("Input search keyword ->->->->->")
base_url = f"https://www.moj-posao.net/Pretraga-Poslova/?keyword={keyword}&area=2&category="

print("\nsearch results\n")

response = get(base_url)
html_soup = BeautifulSoup(response.text, 'html.parser')

try: # Make sure there are more than one page, otherwise, set to 1.
  num_pages = int(re.findall("\d+$", html_soup.find(class_ = "last icon").a.get("href"))[0])
except AttributeError:
  num_pages = 1
#print(num_pages)

url_list = ["{}&page={}".format(base_url, str(page)) for page in range(1, num_pages + 1)]
#print(url_list)


"""
featured = html_soup.find(True, {"id":["featured-jobs"]})
searchlist = html_soup.find(True, {"class":["searchlist"]})

job_company = searchlist.find_all(True, {"class":["job-company"]})
job_position = searchlist.find_all(True, {"class":["job-title", "job-position"]})
job_location = searchlist.find_all(True, {"class":["job-location"]})
job_deadline = searchlist.find_all(True, {"class":["deadline"]})

for a, b, c, d in zip(job_company, job_position, job_location, job_deadline):
  print(a.text.strip())
  print(b.text.strip())
  print("Lokacija: ", c.text.strip())
  print(d.text.strip())
  print("-----------------------------")

https://stackoverflow.com/questions/26497722/scrape-multiple-pages-with-beautifulsoup-and-python
"""