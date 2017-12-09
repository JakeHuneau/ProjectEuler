from math import floor


def day_of_week(year, month, day):
    '''
    Uses Disparate variation of Gaussian algorithm
    w = (d + floor(2.6 m - 0.2) + y + floor(y/4) + floor(c/4) - 2c) mod 7
    y = last 2 digs of year
    c = first 2 digits of year
    d = day of the month (1 - 31)
    m = month (March = 1, ..., Feb = 12)
    w = day of week (0 = Sunday, ..., 6 = Saturday)
    '''
    m = (month - 3) % 12
    if m > 10:
        year -= 1
    y = int(str(year)[-2:])
    c = int(str(year)[:2])
    d = day
    m = (month - 2) % 12

    return int((d + floor(2.6 * m - 0.2) + y + floor(y/4) + floor(c/4) - 2 * c) % 7)


def main():
    total = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if day_of_week(year, month, 1) == 0:
                total += 1
    print(total)


if __name__ == '__main__':
    main()