import requests
from BeautifulSoup import BeautifulSoup

#get search results
def search(url):
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html)

    body = soup.findAll("body")
    full_text = body[0].text
    return full_text