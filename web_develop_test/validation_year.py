__author__ = 'nancy'


def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year > 1900 and year < 2020:
            return year


def main():
    print valid_year('1970')

if __name__=='__main__':
    main()