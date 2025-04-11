import numbers

from numpy import append


def main():
    N = int(input('Enter the number N: '))
    result = []
    z=1
    i=0
    
    for i in range(N+1):
        result.append(2 ** i)

    print(result)
    
    

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
