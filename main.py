def main():
    z=1
    i=0
    N = int(input('Enter the number N: '))
    result = []
    
    for i in range(N):
        
        z=z+z
        i=i+1
        result=z
        print(result, end=" ")

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
