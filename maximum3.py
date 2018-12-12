def maximum3(n1,n2,n3):
    """Objective : To find out maximum of 3 numbers"""
    if n1 > n2:
        if n1 > n3:
            maxnumber = n1
        else:
            maxnumber = n3
    elif n2 > n3:
        maxnumber = n2
    else:
        maxnumber = n3
        
    return maxnumber

def main():
    n1 = int(input("Enter the first number"))
    n2 = int(input("Enter the second number"))
    n3 = int(input("Enter the third number"))
    maximum = maximum3(n1,n2,n3)
    print("The maximum of ",n1,n2,n3, " is ",maximum)

if __name__ == "__main__":
    main()