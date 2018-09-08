def word_val(word):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    str_val = ''
    for l in word:
        indx = letters.find(l) + 1


words = [w.strip('"') for w in open('p098_words.txt').readline().split(',')]