def check_palindrome(st):
    return str(st) == str(st)[::-1]
    
def add_reverse(i):
    return i + int(str(i)[::-1])
    
def check_lychrel(i, iterations):
    lychrel = True
    i = add_reverse(i)
    for n in range(iterations):
        if check_palindrome(i):
            lychrel = False
            break
        i = add_reverse(i)
    return lychrel
        
def check_lychs(check_to):
    lychs = []
    for i in range(1, check_to+1):
        if check_lychrel(i, 50):
            lychs.append(i)
    return lychs
    
if __name__ == '__main__':
    lychs = check_lychs(10000-1)
    print(len(lychs))