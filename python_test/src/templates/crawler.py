__author__ = 'nancy'

from urllib import urlopen
from bs4 import BeautifulSoup
from urlparse import urljoin, urlparse
from os import makedirs, path


def save_content(html, url):
    p = urlparse(url).path
    print "++++++++++++++++++++++", p
    if p[-1:] == "/":
        p += "slide_test_04_formal.html"

    save_path = path.join("/tmp/test", p[1:])
    dirs = path.dirname(save_path)

    if not path.exists(dirs):
        makedirs(dirs)

    try:
        open(save_path, 'w').write(html)
        print "save", url, "---->", save_path
    except:
        pass


def get_and_extract_links(url):
    urls = []
    try:
        html = urlopen(url).read()
        save_content(html, url)
        soup = BeautifulSoup(html)
        hrefs = soup.find_all('a')
        for a in hrefs:
            href = a.get('href')
            if href:
                href = href.strip()
            if href:
                # print(href, urljoin(url, href))
                print(href,'@@@@@@@@@@@@@@@@@@@@@@')
                u = urljoin(url, href)
                print(u,'[[[[[[[[[[[[[[[[[[[[[[[')
                if "#" in u:
                    u = u[:u.index("#")]
                urls.append(u)
        print(urls)
    except Exception as e:
        print("ERROR", e)
    return urls


def main():
    seed = 'http://www.baidu.com'
    to_be_download = [seed]
    downloaded = set()
    while to_be_download:
        url = to_be_download.pop()
        print "download", url, "has", len(to_be_download), "urls remaining", "downloaded", len(downloaded)
        urls = get_and_extract_links(url)
        downloaded.add(url)
        for url in urls:
            if seed in url and url[:4] == "http" and url not in downloaded:
                print "add", url
                to_be_download.append(url)


if __name__ == '__main__':
    main()
