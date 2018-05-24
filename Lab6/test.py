#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''

import requests
from bs4 import BeautifulSoup


def soup_test(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html5lib')

    return soup.find('table')
        

if __name__ == '__main__':
    url = 'http://catalog.oregonstate.edu/CourseDetail.aspx?subjectcode=MUS&coursenumber=102'
    
    rates = soup_test(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html5lib')
    print(soup)