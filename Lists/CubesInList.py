def main():
    '''This is a program to generate a list of cube of first 10 natural numbers'''
    num = 10
    cubes = []
    for i in range(1,num+1):
        cubes.append(i **3)
    print(cubes)

if __name__ == '__main__':
    main()
