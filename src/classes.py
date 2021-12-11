import requests
from bs4 import BeautifulSoup
import pandas as pd

class WikiPage(object):
    def __init__(self, link, title = ''):
        self.link = link
        self.title = title

    def __str__(self):
        return f"{self.link} [{self.title}]"

    def __eq__(self, other):
        return self.link == other.link

    def makeUrl(self):
        return 'https://en.wikipedia.org' + self.link

    def crawl(self, only_link=False):
        def isValid(link, title):
            if link == None or title == None:
                return False
            else:
                return not any(['wiki' not in link, ':' in link, 'wikipedia' in link, 'Main_Page' in link, 'identifier' in link])
        reqs = requests.get(self.makeUrl())
        soup = BeautifulSoup(reqs.text, 'html.parser')
        edges = {'src':[], 'dest': []}
        for child in soup.find_all('a'):
            if isValid(child.get('href'), child.get('title')):
                if only_link:
                    if child.get('href') not in edges['dest']:
                        edges['src'].append(self.link)
                        edges['dest'].append(child.get('href'))
                else:
                    if WikiPage(child.get('href'), child.get('title')) not in edges['dest']:
                        edges['src'].append(self)
                        edges['dest'].append(WikiPage(child.get('href'), child.get('title')))
        return edges

    def make_csv(self):
        dest_pages = self.crawl(only_link=True)
        out_file = open(f'data/{self.title}.csv', 'w')
        out_frame = pd.DataFrame(dest_pages)
        out_frame.to_csv(out_file)
        out_file.close()
        return dest_pages