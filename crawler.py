import requests
from BeautifulSoup import BeautifulSoup

#get search results
query_word = "whales"
url = "https://quizlet.com/subject/" + query_word + "/"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)
search_results_list = soup.findAll("a", { "class" : "UILink" })

#scrape those search results
for link in search_results_list:
    url = link['href']
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html)
    list_of_words = soup.findAll('span', {"class" : "TermText notranslate lang-en qWord"})
    list_of_defs = soup.findAll('span', {"class" : "TermText notranslate lang-en qDef"})
    flashcards = {}
    for set in list_of_words:
        flashcards[list_of_words[set]] = list_of_defs[set]