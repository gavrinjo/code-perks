from bs4 import BeautifulSoup as bS
from requests import get
# from requests.exceptions import RequestException, Timeout, TooManyRedirects, HTTPError
from contextlib import closing
# import json
# import re
# from datetime import datetime, timedelta


class Source:
    def __init__(self, url):
        self.url = url

    def raw_data(self):
        with closing(get(self.url, stream=True)) as f:
            if self.response_check(f):
                return f.content
            else:
                self.log_error(f)

    @staticmethod
    def response_check(f):
        content_type = f.headers["Content-Type"].lower()
        return f.status_code == 200 and content_type is not None

    @staticmethod
    def log_error(f):
        exit(f"ERROR, check your URLs, invalid response code \"{f.status_code}\"")

    def bs_data(self):
        soup_data = bS(self.raw_data(), "lxml")
        return soup_data.prettify()


class Article(Source):
    def __init__(self, url):
        Source.__init__(self, url)


base_url = "https://www.oglasnik.hr/stanovi-prodaja"
# ?page=2
raw_data = Article(base_url)
print(raw_data.bs_data())
