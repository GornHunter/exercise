__author__ = 'nancy'

def valid_day(day):
    if day and day.isdigit():
        day=int(day)
        if day>0 and day<=31:
            return day

def main():
    print valid_day('31 ')

if __name__=='__main__':
    main()
