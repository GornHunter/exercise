__author__ = 'nancy'
# first = s.find_all('div', {'class': 'Sense'})[0]
# {'type': 'noun', 'sense': [{'def': get_def(first), 'examples': get_exmaples(first)}]}
# dir(soup)
# get_text

# ssh feng@192.168.1.101
# cd ~/Downloads/www.ldoceonline.com

from urllib2 import urlopen
from bs4 import BeautifulSoup
from urlparse import urlparse, urljoin
from os import makedirs, path
import logging

CHARSET = 'charset='
URL_HISTORY = "/tmp/downloaded_urls"
SAVE_DIR = '/tmp/crawler'


def save_content(html, url):
    p = urlparse(url).path
    if not p:
        p += '/slide_test_04_formal.html'
    if p[-1:] == '/':
        # print(p)
        p += 'slide_test_04_formal.html'
        # print(p)
    save_path = path.join(SAVE_DIR, p[1:])
    dirs = path.dirname(save_path)

    if not path.exists(dirs):
        makedirs(dirs)

    open(save_path, 'w').write(url.encode('utf8') + '\n' + html.encode('utf8'))
    print 'save', url, '---->', save_path


def get_extracted_link(html, url):
    # print(url)

    soup = BeautifulSoup(html)
    addresses = set()
    # print soup.prettify()
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            href = href.strip()
            if href:
                u = urljoin(url, href)
                # print(url,'-------------')
                # print(href,'+++++++++++')
                # print(u,'[[[[[[[[[[[[[[')
                #
                # if href is not '#' and href is not '/' and href is not '/duty/':
                #     # print(href)
                idx = u.find('#')
                if idx > 0:
                    u = u[:idx]
                addresses.add(u)
                # print(addresses)
    return addresses

#
# def retrieve_wrod_meaning(html):
#     layout = BeautifulSoup(html)
#     for pos in layout.find_all('class'):
#         word_class=pos.get('')

def resume_from_last():
    to_be_download = set()
    downloaded = set()
    try:
        for line in open(URL_HISTORY, 'r'):
            downloaded.add(line.strip())

        import glob
        from os import path

        for f in glob.glob(SAVE_DIR + '/*') + glob.glob(SAVE_DIR + '/**/*'):
            if path.isdir(f):
                continue
            file = open(f, 'r')
            url = file.readline().strip().decode('utf8')
            html = file.read().decode('utf8')
            # retrieve_wrod_meaning(html)
            links = get_extracted_link(html, url) # TODO
            for link in links:
                if link not in downloaded:
                    to_be_download.add(link)
    except Exception as e:
        logging.exception(e)

    return to_be_download, downloaded


def main():
    seed = "http://www.ldoce-online.cn"
    to_be_downloaded, download = resume_from_last()
    if seed not in download:
        to_be_downloaded.add(seed)

    print "downloaded", len(download), 'to_be_downloade', len(to_be_downloaded)
    while to_be_downloaded:
        url = to_be_downloaded.pop()
        print 'downloading', url, len(to_be_downloaded), len(download)
        try:
            html = urlopen(url, "", 1.8).read()
            charset = 'utf8'
            if CHARSET in html:
                start = html.index(CHARSET) + len(CHARSET)
                end = html.index('"', start)
                charset = html[start:end]

            try:
                html = html.decode(charset)
            except Exception as e:
                try:
                    html = html.decode('gbk')
                except Exception as e:
                    logging.exception("decode %s", url)

            save_content(html, url)
            urls = get_extracted_link(html, url)
            open(URL_HISTORY, 'aw').write(url + "\n")
            download.add(url)
            for url in urls:
                if url.find(seed) == 0 and url not in download:
                    # print 'adding', url
                    to_be_downloaded.add(url)

        except Exception as e:
            logging.exception("downloading %s", url)


if __name__ == '__main__':
    main()
