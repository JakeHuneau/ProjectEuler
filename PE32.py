def main():
    prods = set()
    for i in range(100):
        for j in range(5000):
            if ''.join(sorted(str(i)+str(j)+str(i*j))) == '123456789':
                prods.add(i*j)
    print(sorted(prods))
    print(len(prods))
    print(sum(prods))

def is_pandigital(n, s=9): n=str(n); return len(n)==s and not '1234567890'[:s].strip(n)

if __name__ == '__main__':
    main()