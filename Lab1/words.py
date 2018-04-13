def letter_count(string1, string2):
    """Counts the number of occurents of string 2 inside string 1."""
    '''Count function found from search: 
    https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string'''
    '''case sensitivity found from search:
    https://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison'''


    num = string1.lower().count(string2.lower())
    return num

if __name__ == '__main__':
    print(letter_count('halLway','l'))
    print(letter_count('halLway','L'))