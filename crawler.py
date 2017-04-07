import requests
from BeautifulSoup import BeautifulSoup

#get search results
query_word = "Whale"
url = "https://en.wikipedia.org/wiki/" + query_word
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

body = soup.findAll("body")
full_text = body[0].text