import re

def filter_word(a):
    with open('filtered_words.txt', 'r', encoding = 'utf-8') as f:
        f = f.read()
        if a == '':
            print('Right')

        if len(re.findall(r'%s' % (a), f)) == 0:
            print('Right')

        else:
            print('Error')

z = input('Input:')
filter_word(z)
