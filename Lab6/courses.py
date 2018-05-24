#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''

import requests


class Course:
    def __init__(self, course_data):
        if isinstance(course_data, list):
            pass
        else:
            raise TypeError('Course Data must be a list')
        self.course_data = course_data

    def __str__(self):
        return '{} {}: {}'.format(self.course_data[0], self.course_data[1], self.course_data[2])

    def credit(self):
        return self.course_data[3]

    def term(self):
        return self.course_data[4][0]

    def CRN(self):
        return self.course_data[5][0]

    def section(self):
        return self.course_data[6][0]

    def prof(self):
        return self.course_data[7][0]

    def days(self):
        return self.course_data[8][0]

    def time(self):
        return self.course_data[9][0]

    def room(self):
        return self.course_data[10][0]

    def campus(self):
        return self.course_data[11][0]

    def course_type(self):
        return self.course_data[12][0]

def fetch_info(subject, courseCode, term_fetch):
    '''

    :param subject:
    :param courseCode:
    :param term_fetch:
    :return:
    '''
    if isinstance(courseCode, int):
        if len(str(courseCode)) == 3:
            pass
    else:
        raise TypeError('Course code must be an integer of length 3')

    url = 'http://catalog.oregonstate.edu/CourseDetail.aspx?subjectcode={}&coursenumber={}'.format(subject.upper(), courseCode)
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
            else:
                course_type.append('Other')

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
    days = []
    time = []
    for i in range(len(data)):
        if '</font></td><td nowrap="nowrap"><font size="2">' in data[i]:

            a = data[i].find('</font></td><td nowrap="nowrap"><font size="2">')
            b = data[i][a + 47::]

            if 'Corv' in b or 'Casc' in b or 'Ecampus-Distance Education-LD' in b:
                campus.append(b)
            else:
                prof.append(b)
            if '                        ' in data[i+2]:
                if 'TBA' in data[i+2]:
                    days.append(data[i+2].strip(' ').replace('\r',''))
                    time.append(data[i+2].strip(' ').replace('\r',''))
                else:
                    line = data[i+2].replace('<', ' ').replace('>', ' ').strip(' ').split(' ')
                    days.append(line[0])
                    time.append(line[1])

    for i in range(len(prof)):
        idx = prof[i].find('</font>')
        prof[i] = prof[i][0:idx]

    for i in range(len(campus)):
        idx = campus[i].find('<')
        campus[i] = campus[i][0:idx]

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
            elif 'Recitation':
                course_type.append('Recitation')
    # print(course_type)

    for i in range(len(course_type)):
        if term[i] != term_fetch or course_type[i] != 'Online' and course_type[i] != 'Lecture':
            term[i] = ''
            CRN[i] = ''
            section[i] = ''
            prof[i] = ''
            days[i] = ''
            time[i] = ''
            room[i] = ''
            campus[i] = ''
            course_type[i] = ''


    term = list(filter(None, term))
    CRN = list(filter(None, CRN))
    section = list(filter(None, section))
    prof = list(filter(None, prof))
    days = list(filter(None, days))
    time = list(filter(None, time))
    room = list(filter(None, room))
    campus = list(filter(None, campus))
    course_type = list(filter(None, course_type))
    course_data = [depart, courseNum, descr, credit, term, CRN, section, prof, days, time, room, campus, course_type]

    return Course(course_data)

if __name__ == '__main__':

    a = fetch_info('ME', 451, 'F18')
    print(a)

    b = fetch_info('ROB', 514, 'F18')
    print(b)

    c = fetch_info('ME', 312, 'W19')
    print(c)

    d = fetch_info('MUS', 102, 'W19')
    print(d)

    e = fetch_info('Bi', 315, 'Sp19')
    print(e)






