import requests 
import re
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/'
#url = 'https://example.com'
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

print(soup.title.get_text())
print(soup.find(class_="title"))

result = soup.find_all(class_="is-5")

for html in result:
    soft_related = re.findall('.*Software.*',str(html)) #any title that mentions Software
    if soft_related != []:
        print(soft_related)

head_div = soup.find_all(re.compile("(head|div)")) #anything inside a head or a div tag
print(head_div)