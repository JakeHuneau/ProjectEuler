import numpy as np

def GenFibo(x):
    '''
    Generates a list of the fibonacci sequence that are less than x
    -Inputs-
    x: (Int) max value in the Fibonacci sequence
    -Returns-
    fiboList: (list of ints) Fibonacci sequence
    '''
    fiboList = [1]
    f = 1
    while f < x:
        fiboList.append(f)
        f += fiboList[-1]
    return fiboList
    
def findEvenValues(Arr):
    '''
    Returns even values from list
    '''
    return [x if x%2 == 0 else 0 for x in Arr]
    
if __name__ == "__main__":
    print(sum(findEvenValues(GenFibo(4000000))))