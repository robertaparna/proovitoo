from requests_html import HTMLSession
import bs4


def get_text_content(soup):
    #parsib htmlist välja kõik teksti ja ühendab selle stringiks
    text_content = []
    for text in soup.find_all(string=True):
        text_stripped = text.text.strip()
        if text_stripped and text_stripped not in text_content :
            text_content.append(text.text.strip())
    return text_content


class Crawler:

    source_info = {}

    def __init__(self, url):
        s = HTMLSession()
        #pärib lehe sisu
        r = s.get(url)

        soup_main = bs4.BeautifulSoup(r.text, 'lxml')

        sub_pages = []

        #otsib lehelt välja olulised alamlehed
        for link in soup_main.find_all('a'):
            sub_url = link.get('href')
            if (sub_url and 'tehisintellekt' in sub_url
                    and sub_url not in sub_pages
                    and '#' not in sub_url
                    and 'artiklid' not in sub_url
                    and sub_url.startswith('http')
                    and sub_url != url):
                sub_pages.append(sub_url)

        #salvestab lehelt teksti
        self.source_info[url] = ' '.join(get_text_content(soup_main))

        for sub_url in sub_pages:
            #salvestab teksti alamlehtedelt
            r = s.get(sub_url)
            soup = bs4.BeautifulSoup(r.text, 'lxml')
            self.source_info[sub_url] = ' '.join(get_text_content(soup) )


    def get_source_info(self):
        return self.source_info
