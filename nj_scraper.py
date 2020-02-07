from bs4 import BeautifulSoup as bs
from requests import get
import lxml
import re

url = "https://www.njuskalo.hr/prodaja-stanova/zagreb?price%5Bmin%5D=5000&price%5Bmax%5D=133000&includeOtherCategories=1&livingArea%5Bmin%5D=70&adsWithImages=1&flatBuildingType=flat-in-residential-building&balconyInfo=allthree&buildingFloorPosition%5Bmin%5D=1&page=1"

raw_data = get(url)
soup_data = bs(raw_data.text, "html.parser")


def open_file(src):
    with open(src, "w", encoding="utf8") as file:
        file.write(str(soup_data.prettify()))


def article_title(src):
    open_file(src)
    for article in soup_data.find_all("div", class_="col-md-3"):
        print(article.img.get("alt"))


if __name__ == "__main__":
    article_title("test1.html")
