__author__ = 'feng'

from urllib import urlopen
from urlparse import urljoin, urlparse
from os import makedirs, path

from bs4 import BeautifulSoup

def save_content(html, url):
    p = urlparse(url).path
    if p[-1:] == "/":
        # "http://google.com/" => "http://google.com/slide_test_04_formal.html"
        p += "slide_test_04_formal.html"

    save_path = path.join("/tmp/shenfeng_www", p[1:])
    dirs = path.dirname(save_path)

    if not path.exists(dirs):
        makedirs(dirs)

    try:
        open(save_path, 'w').write(html)
        print "save", url, "---->", save_path
    except:
        pass


def get_and_extract_links(url):
    html = urlopen(url).read()
    urls = []
    save_content(html, url)
    try:
        soup = BeautifulSoup(html)
        hrefs = soup.find_all('a')
        for a in hrefs:
            href = a.get('href')
            if href:
                href = href.strip()
            if href:
                urls.append(urljoin(url, href))
        print "downloaded", url, "find", len(urls), "new urls"
    except Exception as e:
        print "ERROR", e

    return urls, html



def main():
    seed = 'http://www.ldoceonline.com/School-topic/master_1'
    seed = 'http://http-kit.org/'

    to_be_downloaded = [seed]

    downloaded = set()

    while to_be_downloaded:
        url = to_be_downloaded.pop()
        print "download", url, "has", len(to_be_downloaded), "urls remaining", "downloaded", len(downloaded)
        urls, html = get_and_extract_links(url)
        downloaded.add(url)
        for url in urls:
            if seed in url and url[:4] == "http" and url not in downloaded:
                to_be_downloaded.append(url)


if __name__ == '__main__':
    main()

