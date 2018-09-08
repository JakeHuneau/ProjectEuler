from PE18 import add_from_under
import time


def break_pyramid(num_pyr):
    '''
    Breaks the number string into an array
    '''
    pyramid = []
    rows = num_pyr.split('\n')
    for row in rows[:-1]:  # Last line is empty
        pyramid.append([int(i) for i in row.split(' ')])
    return pyramid


def main():
    with open('p067_triangle.txt', 'r') as pyramid_file:
        pyramid_str = pyramid_file.read()
    pyramid = break_pyramid(pyramid_str)[::-1]
    for i in range(len(pyramid)-1):
        new_upper = add_from_under(pyramid[1], pyramid[0])
        pyramid[1] = new_upper
        del pyramid[0]
    return pyramid[0][0]

if __name__ == '__main__':
    t1 = time.time()
    best_path = main()
    op_time = 1000 * (time.time() - t1)  # ms
    print("Calculated {} in {:.4f} ms".format(best_path, op_time))
