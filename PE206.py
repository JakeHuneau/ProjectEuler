# Form is 1_2_3_4_5_6_7_8_9_0
# lower bound is 1000000000
# upper bound is 4472135954
# Must end in 0 so final 2 numbers of square are 00. So we can search for sqrt of 1_2_3_4_5_6_7_8_9
# and multiply by 10
# lower bound is 1e8 amd upper is 141421356 giving 41421356 possible numbers and number must end in 3 or 7
# So just going to brute force

def check_form(num):
    num = str(num)
    if num[0] == '1':
        if num[2] == '2':
            if num[4] == '3':
                if num[6] == '4':
                    if num[8] == '5':
                        if num[10] == '6':
                            if num[12] == '7':
                                if num[14] == '8':
                                    if num[16] == '9':
                                        return True
    return False


n = 100000003
add_iter = 0

while True:
    if check_form(n ** 2):
        print(n * 10)
        break
    else:
        if add_iter == 0:
            n += 4
            add_iter = 1
        elif add_iter == 1:
            n += 6
            add_iter = 0
        else:
            print('what')
            break