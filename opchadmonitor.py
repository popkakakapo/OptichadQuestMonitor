import requests as r
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import re
import smtplib
#import yagmail
import json
import time

url = 'https://app.quest3.xyz/OptiChads'

page = urlopen(url)
html = page.read().decode("utf-8")
result = soup(html, "html.parser")

print(result)


