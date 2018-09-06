from collections import Counter

def main():
    encoded = list(map(int, open('p059_cipher.txt', 'r').read().split(',')))

    ascii_space = ord(' ')

    enc_count = [Counter(encoded[i::3]) for i in range(3)]
    most_common_enc = [count.most_common(1)[0][0] for count in enc_count]
    key = [most_common ^ ascii_space for most_common in most_common_enc]

    print(sum(e ^ k for e, k in zip(encoded, key * (len(encoded) // 3 + 1))))


if __name__ == '__main__':
    main()
