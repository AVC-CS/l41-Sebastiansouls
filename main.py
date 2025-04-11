def main():
    N = int(input('Enter the number N: '))
    result = []
    z=1
    i=0
    N=N+1
    for i in range(N):
        result=z
        print(result, end=" ")
        z=z+z
        i=i+1

        
    
    

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
