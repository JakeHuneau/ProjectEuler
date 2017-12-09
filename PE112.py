def is_bouncy(num):
    num_list = [int(x) for x in str(num)]
    sort_list = sorted(num_list)
    if num_list != sort_list and num_list != sort_list[::-1]:
        return True
    else:
        return False
        
if __name__ == '__main__':
    bouncy_nums = []
    i = 100
    while True:
        if is_bouncy(i):
            bouncy_nums.append(i)
        if len(bouncy_nums) / i > 0.99:
            print(i-1)
            break
        i += 1