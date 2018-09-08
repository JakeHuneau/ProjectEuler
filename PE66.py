from Project_Euler import smallest_pells_soln


def main():
    x_max = 1
    d_max = 1
    for i in range(1, 1001):
        x, y = smallest_pells_soln(i)
        if x > x_max:
            x_max = x
            d_max = i
    print(d_max)


if __name__ == '__main__':
    main()
