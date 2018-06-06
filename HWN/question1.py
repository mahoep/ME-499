#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''


def is_power(a, b):
    c = a/b
    remainder = a % b
    if c == 1:
        return True
    elif remainder != 0:
        return False
    else:
        return is_power(c, b)


if __name__ == '__main__':

    # def rnum():
    #     a = np.random.randint(1, 10)
    #     b = np.random.randint(1, 3)

    print(is_power(2, 2))
    print(is_power(3, 2))
    print(is_power(4, 2))
    print(is_power(5, 2))
    print(is_power(2, 3))
    print(is_power(3, 3))
    print(is_power(4, 3))
