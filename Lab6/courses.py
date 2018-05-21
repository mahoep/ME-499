#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''


import requests
from bs4 import BeautifulSoup
class Course:

    def __init__(self, url):
        if isinstance(url, str):
            pass
        else:
            raise TypeError('URL must be a str')
        self.url = url

    def fetch(self):
        response = requests.get(self.url)
        start = '<h3>'
        end = '</h3>'
        start_idx = response.text.find(start)
        end_idx = response.text.find(end)
        h3 = response.text[start_idx:end_idx]

        header_start = '\n'
        info = h3[h3.find(header_start, 10)::].split()

        depart = info[0]
        courseNum = info[1].strip('.')
        descr = " ".join(str(x) for x in info[2:-1])
        credit = info[-1].strip('()').strip('.').strip(')')
        self.header = [depart, courseNum, descr]

    def fetch_bs4(self):
        response = requests.get(self.url)
        text = response.text
        soup = BeautifulSoup(text, 'html.parser')
        h3 = str(soup.h3).split('\n')

        catalogNum = h3[2].strip(' ').replace('.', '')
        depart = catalogNum.split(' ')[0]
        courseNum = catalogNum.split(' ')[1]
        descr = h3[3].strip(' ')
        credit = h3[4].strip(' ').replace('.', '').lstrip('(').replace(')', '')
        self.header = [depart, courseNum, descr]


    def __str__(self):
        Course.fetch(self)
        return '{} {}: {}'.format(self.header[0], self.header[1], self.header[2])


    def prof(self):
        response = requests.get(url)
        data = response.text.split('\n')
        self.prof = []
        for i in data:
            if '</font></td><td nowrap="nowrap"><font size="2">' in i:
                a = i.find('</font></td><td nowrap="nowrap"><font size="2">')
                b = i[a + 47:a + 75]
                if 'Corv' not in b:
                    self.prof.append(i[a + 47:a + 75])
        for i in range(len(self.prof)):
            idx = self.prof[i].find('.')
            self.prof[i] = self.prof[i][0:idx + 1]
        return self.prof

    def info(self):
        response = requests.get(url)
        data = response.text.split('\n')
        term = []
        CRN = []
        section = []
        for i in data:
            if '<td align="right"><font size="2">' in i:
                line = i.split('<')
                term_raw = line[2]
                idx = term_raw.find('>')
                term.append(term_raw[idx + 1::])

                CRN_raw = line[6]
                idx = CRN_raw.find('>')
                CRN.append(CRN_raw[idx + 1::])

                section_raw = line[10]
                idx = section_raw.find('>')
                section.append(section_raw[idx + 1::])
        self.info = [term, CRN, section]
        return self.info

# def scrape_course(depart, courseNum, term):
if __name__ == '__main__':
    url = 'http://catalog.oregonstate.edu/CourseDetail.aspx?subjectcode=ME&coursenumber=430'


    c = Course(url)
    print(c.info())