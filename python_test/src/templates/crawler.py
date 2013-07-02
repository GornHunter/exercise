__author__ = 'nancy'

def main():
    seed='http://www.boomsense.com'

    to_be_download=[seed]

    downloaded=set()

    while to_be_download:
        url = to_be_download
