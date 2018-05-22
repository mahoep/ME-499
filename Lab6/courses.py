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

    def __str__(self):
        Course.fetch(self)
        return '{} {}: {}'.format(self.header[0], self.header[1], self.header[2])



    def fetch_info(self):
        response = requests.get(url)
        data = response.text.split('\n')
        courseInfo = []
        count = 0
        for i in data:
            count += 1
            if '<img alt="Course" src="images/icon/courselg.gif" border="0" style="font-weight: bold" />' in i:
                for j in range(0, 3):
                    courseInfo.append(data[count + j])

        self.depart = courseInfo[0].strip(' ').split(' ')[0]
        self.courseNum = courseInfo[0].strip(' ').split(' ')[1].replace('.', '').strip()
        self.descr = courseInfo[1].strip(' ').strip()
        self.credit = courseInfo[2].strip(' ').replace('.', '').strip()

        self.term = []
        self.CRN = []
        self.section = []
        for i in data:
            if '<td align="right"><font size="2">' in i:
                line = i.split('<')
                term_raw = line[2]
                idx = term_raw.find('>')
                self.term.append(term_raw[idx + 1::])

                CRN_raw = line[6]
                idx = CRN_raw.find('>')
                self.CRN.append(CRN_raw[idx + 1::])

                section_raw = line[10]
                idx = section_raw.find('>')
                self.section.append(section_raw[idx + 1::])

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

        for i in data:
            if '<td align="right" valign="top" nowrap="nowrap"><font size="2">' in i:
                print(i)

        return [self.depart, self.courseNum, self.descr, self.credit, self.term, self.CRN, self.section, self.prof]


# def scrape_course(depart, courseNum, term):
if __name__ == '__main__':
    url = 'http://catalog.oregonstate.edu/CourseDetail.aspx?subjectcode=ME&coursenumber=451'


    # c = Course(url)
    # print(c.fetch_info())
    response = requests.get(url)
    data = response.text.split('\n')
    for i in data:
        if '<BR />' in i.strip(' '):
            line = i.replace('<', ' ').replace('>', ' ')
            print(line)

