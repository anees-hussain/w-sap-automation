import requests
from bs4 import BeautifulSoup
from time import sleep

url = "http://cciwebsap.cci.tr/"

res = requests.get(url)
htmlContent = res.content

soup = BeautifulSoup(htmlContent, 'html.parser')