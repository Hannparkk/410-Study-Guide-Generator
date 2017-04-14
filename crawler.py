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

def write_doc_to_file(filename, url):
    f = open(filename, "w+")
    full_text = search(url)
    f.write(full_text.encode('utf-8'))
    f.close()

write_doc_to_file("whale_doc17", "https://en.wikipedia.org/wiki/Beluga_whale")