from bs4 import BeautifulSoup as bs
from requests import get
# from requests.exceptions import RequestException
from contextlib import closing
import json
import re
from datetime import datetime, timedelta


class Source:
    def __init__(self, source):
        self.source = source

    def url(self):
        with closing(get(self.source, stream=True)) as f:
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
        soup_data = bs(self.url(), "lxml")
        print(soup_data)

    def print_source(self):
        print(self.url())


base_url = "https://www.oglasnik.hr/stanovi-prodaja"
# ?page=2
raw_data = Source(base_url)
# raw_data.print_source()
raw_data.bs_data()
