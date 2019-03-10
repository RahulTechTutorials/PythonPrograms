def main():
    n = int(input("Enter the number for the Multiplication chart"))
    for i in range(1,11):
        print(n,  ' * ' ,'%2d' %i, ' = ', '%5d'%(n*i) )

if __name__ == "__main__":
    main()