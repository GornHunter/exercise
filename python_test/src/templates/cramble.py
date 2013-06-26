__author__ = 'feng'

from urllib import urlopen
from urlparse import urljoin

from bs4 import BeautifulSoup


def get_next_urls(urls):
    pass


def get_and_extract_links(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html)
    hrefs = soup.find_all('a')
    urls = []
    for a in hrefs:
        href = a.get('href')
        if href:
            href = href.strip()
        if href:
            urls.append(urljoin(url, href))
    return urls, html


def save_html(url, html):
    pass


def main():
    seed = 'http://www.ldoceonline.com/School-topic/master_1'
    seed = 'http://www.merriam-webster.com/dictionary/denoting'

    to_be_downloaded = [seed]

    while to_be_downloaded:
        url = to_be_downloaded.pop()
        urls, html = get_and_extract_links(url)
        save_html(seed, html)
        for url in urls:
            if "dictionary/" in url:
                to_be_downloaded.append(url)


if __name__ == '__main__':
    main()
__author__ = 'nancy'
