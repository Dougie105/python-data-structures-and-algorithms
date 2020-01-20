from collections import Counter


def punctuation(str):
    '''Gets rid of punctuation in a string.'''
    punc = '!@#$%^&*()_-+=[{]};:,./?`<>"~'
    new_str = ""

    for i in str:
        if i not in punc:
            new_str += i
    return new_str


def repeated_word(str):
    '''Finds first repeated word in a given string.'''
    string = punctuation(str)
    string = string.casefold()
    new_str = string.split(" ")
    dict = Counter(new_str)

    for key in new_str:
        if dict[key] > 1:
            return key
    return False
