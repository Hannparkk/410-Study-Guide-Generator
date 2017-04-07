import requests
from BeautifulSoup import BeautifulSoup

#get search results
query_word = "Whale"
url = "https://en.wikipedia.org/wiki/" + query_word
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

scrape_anything = soup.findAll("h2")
for header in scrape_anything:
    print header.text