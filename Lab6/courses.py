#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''


import requests
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

    def __str__(self):
        Course.fetch(self)
        return '{} {}: {}'.format(self.header[0], self.header[1], self.header[2])



def scrape_course(depart, courseNum, term)
if __name__ == '__main__':
    url = 'http://catalog.oregonstate.edu/CourseDetail.aspx?subjectcode=ME&coursenumber=451'

    c = Course(url)
    print(c)

    c = scrape_course('ME', '451', 'W18')
    print(c)