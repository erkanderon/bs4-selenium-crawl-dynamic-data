from bs4 import BeautifulSoup
from selenium import webdriver

import requests

driver = webdriver.Firefox(executable_path='/home/erkanderon/Desktop/DjangoApplications/tutorial_projects/scrapyexample/geckodriver')
driver.get('https://iddaa.com/futbol-programi/')
url= "http://blog.stevensanderson.com/2009/08/24/writing-great-unit-tests-best-and-worst-practises/"
r  = requests.get(url)

html = driver.page_source
soup = BeautifulSoup(html)

data = r.text

soup = BeautifulSoup(html, "html.parser")

##for link in soup.find_all('p'):
##    print(link.text)

for link in soup.find_all('a'):
    print(link)
