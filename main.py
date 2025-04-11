def main():
    z=1
    i=0
    N = int(input('Enter the number N: '))
    result = []
    
    for i in range(N):
        print(z, end=" ")
        z=z+z
        i=i+1

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
