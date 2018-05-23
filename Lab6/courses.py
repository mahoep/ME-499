#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''


import requests
# from bs4 import BeautifulSoup
class Course:

    def __init__(self, course_data):
        if isinstance(course_data, list):
            pass
        else:
            raise TypeError('Course Data must be a list')
        self.course_data = course_data

    def __str__(self):
        return '{} {}: {}'.format(self.course_data[0], self.course_data[1], self.course_data[2])

    def prof(self, term=0):
        return self.course_data[7]


def fetch_info(url, term_id='all'):
    '''
    :param url: URL to OSU course catalog of specific class
    :param term_id: defines which term the function will return, default is all that are listed
        no matter the term_id, value all will be fetched
    :return: Information regarding course on OSU website
    '''
    response = requests.get(url)
    data = response.text.split('\n')
    courseInfo = []
    count = 0
    for i in data:
        count += 1
        if '<img alt="Course" src="images/icon/courselg.gif" border="0" style="font-weight: bold" />' in i:
            for j in range(0, 3):
                courseInfo.append(data[count + j])

    depart = courseInfo[0].strip(' ').split(' ')[0]
    courseNum = courseInfo[0].strip(' ').split(' ')[1].replace('.', '').strip()
    descr = courseInfo[1].strip(' ').strip()
    credit = courseInfo[2].strip(' ').replace('.', '').strip()

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

    prof = []
    campus = []
    for i in data:
        if '</font></td><td nowrap="nowrap"><font size="2">' in i:
            a = i.find('</font></td><td nowrap="nowrap"><font size="2">')
            b = i[a + 47:a + 75]

            if 'Corv' not in b or 'Casc' not in b or 'Ecampus-Distance Education-LD' not in b:
                prof.append(i[a + 47:a + 75])
            if 'Corv' in b or 'Casc' in b or 'Ecampus-Distance Education-LD' in b:
                campus.append(i[a + 47:a + 75])
    for i in range(len(prof)):
        idx = prof[i].find('.')
        prof[i] = prof[i][0:idx + 1]

    for i in range(len(campus)):
        idx = campus[i].find('<')
        campus[i] = campus[i][0:idx]
    prof = [x for x in prof if x]


    days = []
    time = []
    dates = []
    for i in data:
        if '<BR />' in i.strip(' '):
            line = i.replace('<', ' ').replace('>', ' ').strip(' ').split(' ')
            days.append(line[0])
            time.append(line[1])
            dates.append(line[-1].replace('\r', ''))
            # print(line)

    room = []
    for i in range(len(data)):
        if '</font></td><td align="left" nowrap="nowrap"><font size="2">' in data[i]:
            room.append(data[i + 2].strip(' ').replace('\r', ''))
    course_type = []
    for i in range(len(data)):
        if '</font></td><td valign="top"><font size="2">' in data[i]:
            if 'Lecture' in data[i]:
                course_type.append('Lecture')
            elif 'Laboratory' in data[i]:
                course_type.append('Laboratory')
            elif 'Online' in data[i]:
                course_type.append('Online')
            elif 'Hybrid' in data[i]:
                course_type.append('Hybrid')
    print(course_type)


    course_data = [depart, courseNum, descr, credit, term, CRN, section, prof, days, time, dates, room, campus, course_type]

    return Course(course_data)

if __name__ == '__main__':
    url = 'http://catalog.oregonstate.edu/CourseDetail.aspx?subjectcode=ME&coursenumber=451'

    c = fetch_info(url)
    print(c)
    b = c.prof()
    print(b)
