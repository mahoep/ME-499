#!/usr/bin/env python3


from subprocess import check_output


class Grader(object):
    def __init__(self):
        # Figure out the grading functions
        self.names = [f for f in dir(self) if f[0:6] =='grade_']
        self.func = map(lambda x: getattr(self, x), self.names)
        self.names = [name[6:] for name in self.names]
                        

    def do_grading(self):
        possible = 0
        total = 0
        for f,n in zip(self.func, self.names):
            print('Grading {0}:'.format(n))
            try:
                t,p = f()
                total += t
                possible += p
            except Exception as e:
                print('  could not grade this question')
                print('Error {}'.format(e))
                return
        score = total / possible * 100.0
        
        print('Got {0} total points out of a possible {1}, for {2:.2f}%'.format(total, possible, score))

        return score

    def output_matches(self, command, expected):
        foo = check_output(command.split())
        print(foo)
        return foo.decode('UTF-8') == expected


class Lab0(Grader):
    def grade_Q1(self):
        if self.output_matches('python3 hello.py', 'Hello, World!\n'):
            print('  passed')
            grade = 1
        else:
            print('  failed')
            grade = 0
        return grade,1
    
    def grade_Q2(self):
        if self.output_matches('python3 cylinder.py', '141.3716694115407\n'):
            print('  passed')
            grade = 1
        else:
            print('  failed')
            grade = 0
        return grade,1

    def grade_Q3(self):
        if self.output_matches('python3 torus.py', '17.271807701906376\n'):
            print('  passed')
            grade = 1
        else:
            print('  failed')
            grade = 0
        return grade,1

    
if __name__ == '__main__':
    g = Lab0()
    g.do_grading()
    
