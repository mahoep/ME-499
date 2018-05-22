#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ME 499/599 Spring 2018

Simple web scraping example
Bill Smart
"""

import requests
from bs4 import BeautifulSoup


def get_forex_rates(url):
    response = requests.get(url)
      
    forex = {'EUR': 1.0}
    for line in response.text.split("<Cube currency='")[1:]:
        forex[line[:3]] = float(line.split("'")[2])
    return forex

def get_forex_rates2(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html5lib')

    forex = {'EUR': 1.0}
    for item in soup.find_all('cube'):        
        print(item.get('currency'), item.get('rate'))
        
        try:
            forex[item.get('currency')] = float(item.get('rate'))
        except:
            pass
    return forex
        

if __name__ == '__main__':
    url = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml'
    
    rates = get_forex_rates(url)
    print(rates)