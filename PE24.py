from itertools import permutations

def main():
    nums = '0123456789'
    possible_combs = permutations(nums)
    print(list(possible_combs)[999999])


if __name__ == '__main__':
    main()