def letter_value(s):
    return ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(s)


def word_value(word):
    return sum(letter_value(s) for s in word)


def main():
    with open('p042_words.txt', 'r') as data:
        raw_words_list = data.read().split(',')
    words = [s.strip("'").strip('"') for s in raw_words_list]
    triangle_nums = set([0.5 * n * (n + 1) for n in range(1, 100)])
    word_values = [word_value(word) for word in words]
    count = 0
    for val in word_values:
        if val in triangle_nums:
            count += 1
    print(count)


if __name__ == '__main__':
    main()