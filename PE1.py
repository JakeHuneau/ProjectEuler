def MultiplesUnderX(MultArray,X):
    '''
    Finds all the multiples of each value in MultArray that are below X.
    MultArray: List of ints that multiples are needed of
    X: Int that multiples will go up to
    Ex: MultiplesUnderX([3,5],1000) will return a list of all the multiples of 3 and 5 
    under 1000.
    '''
    return [i if any(i % x == 0 for x in MultArray) else 0 for i in range(X)]
    
if __name__ == "__main__":
    print(sum(MultiplesUnderX([3,5],1000)))