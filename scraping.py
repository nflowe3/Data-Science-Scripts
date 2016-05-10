from bs4 import BeautifulSoup
import requests


url = "http://shop.oreilly.com/category/browse-subject/" + \
	"data.do?sortby=publicationDate&page=1"

html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

print(html)