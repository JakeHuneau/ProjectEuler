import time

def main():
    d = ''
    i = 1
    while len(d) < 1000001:
        d += str(i)
        i += 1
    print(int(d[0]) * int(d[9]) * int(d[99]) * int(d[999]) * int(d[9999]) * int(d[99999]) * int(d[999999]))

if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time() - start)
