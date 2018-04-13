def close(num1, num2, num3):
    """Takes three numbers as arguments. It returns True if the absolute difference between
     ... the first two numbers is less than the third number."""
        if abs(num1 - num2) < num3:
            result = True
            return result
        else:
            result = False
            return result

if __name__ == '__main__':
    print(close(1, 2, 0.5))
    print(close(1, 2, 3))