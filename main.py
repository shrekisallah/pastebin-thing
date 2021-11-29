import requests
from bs4 import BeautifulSoup


# gets html code which includes recent pastes
def gethtml():
    r = requests.get('https://pastebin.com/')
    return r.text


def getrecent():
    # gets html code then parses it
    html = gethtml()
    soup = BeautifulSoup(html, 'html.parser')
    # finds all the links to pastes
    thing = soup.find_all('a')
    soup = BeautifulSoup(str(thing), 'html.parser')
    for link in soup.find_all('a'):
        links = link.get('href')
        if len(links) == 9:
            url = f'https://pastebin.com/raw{links}'
            r = requests.get(url=url)
            with open(f'pastes{links}.txt', 'w') as file:
                file.write(r.text)


def main():
    getrecent()


if __name__ == '__main__':
    main()
