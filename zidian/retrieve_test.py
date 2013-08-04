__author__ = 'nancy'

import glob
from os import path
from bs4 import BeautifulSoup

SAVE_DIR = '/home/nancy/Downloads/www.ldoceonline.com/dictionary'
SAVE_DICT = '/home/nancy/Downloads/worddictionary'

data = {'word': 'filename',
        'type': 'noun',
        'say': 'freqS',
        'write': 'freqW',
        'meaning_exam': [{'meaning': '-----', 'examples': '++++++'},
                         {'meaning': '-----', 'examples': '++++++'},
                         {'meaning': '-----', 'examples': '++++++'}]
}


def every_sense_example(one):
    try:
        every_meaning = one.find('ftdef').get_text()
    except Exception as e:
        every_meaning = None
        print one

    examples = []
    for e in one.find_all('div', {'class': 'EXAMPLE'}):
        example = e.get_text()
        # print example
        examples.append(example)
    return {'meaning': every_meaning, 'examples': examples}


def retrieve_content(soup):
    w = ''
    s = ''
    arr = []
    word_property_arr = []
    word_freq = soup.find_all('div', {'class': 'unfolded'})
    word_sense = soup.find_all('div', {'class': 'Sense'})
    for one in word_sense:
        arr.append(every_sense_example(one))
    for i in soup.find_all('span', {'class': 'POS'}):
        p = i.get_text()
        word_property_arr.append(p)
        # print word_property_arr
    if word_freq:
        word_freqW = word_freq[0].find_all('td', {'class': 'freqW'})
        word_freqS = word_freq[0].find_all('td', {'class': 'freqS'})
        if word_freqW:
            w = word_freqW[0].get('title')
        if word_freqS:
            s = word_freqS[0].get('title')

    return {'type': word_property_arr, 'freqS': s, 'freqW': w, 'examples': arr}


def main():
    dictionary = {}
    for f in glob.glob(SAVE_DIR + '/*')[:100]:
        if path.isdir(f):
            continue
            # print open(f, 'r')
        html = open(f, 'r').read()
        soup = BeautifulSoup(html)
        filename = path.basename(f)
        word = retrieve_content(soup)
        dictionary[filename] = word
    print dictionary
    open(SAVE_DICT, 'w').write(str(dictionary))

if __name__ == '__main__':
    main()