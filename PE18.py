import time

num_pyr = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''


def break_pyramid(num_pyr):
    '''
    Breaks the number string into an array
    '''
    pyramid = []
    rows = num_pyr.split('\n')
    for row in rows:
        pyramid.append([int(i) for i in row.split(' ')])
    return pyramid

def add_from_under(upper_row, lower_row):
    '''
    Takes the maximum of the legs under upper row to each index to add up from bottom
    Parameters
    ----------
    upper_row : len n
    lower_row : len n + 1

    Returns
    -------
    new_upper_row
    '''
    greater_vals = [max(lower_row[i:i+2]) for i in range(len(upper_row))]
    return [x + y for x, y in zip(upper_row, greater_vals)]


def main():
    pyramid = break_pyramid(num_pyr)[::-1]
    for i in range(len(pyramid)-1):
        new_upper = add_from_under(pyramid[1], pyramid[0])
        pyramid[1] = new_upper
        del pyramid[0]
    return pyramid[0][0]


if __name__ == '__main__':
    t1 = time.time()
    best_path = main()
    op_time = 1000000 * (time.time() - t1)  # us
    print("Calculated {} in {:.1f} us".format(best_path, op_time))
