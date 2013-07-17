__author__ = 'nancy'

from urllib import urlopen
from bs4 import BeautifulSoup
from urlparse import urlparse, urljoin


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
            u = urljoin(url, href)
            urls.append(u)
    return urls


def main():
    seed = "http://www.baidu.com"
    url = seed
    to_be_downloaded = [seed]
    downloaded = set()
    while to_be_downloaded:
        url = to_be_downloaded.pop()
        print "download", url, "has", len(to_be_downloaded), "urls remaining", "downloaded", len(downloaded)
        urls = get_and_extract_links(url)
        downloaded.add(url)
        for url in urls:
            if seed in url and url[:4] == 'http' and url in downloaded:
                to_be_downloaded.append(url)


if __name__ == '__main__':
    main()