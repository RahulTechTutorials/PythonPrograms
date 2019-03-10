def main():
    n = int(input("Enter the number of subjects"))
    total_marks = 0
    for i in range(1,n+1):
        marks = int(input("Enter the marks for Subject " + str(i) + ":"))
        total_marks +=  marks
    print("The total marks is " + str(total_marks))
    print("The average marks is " + str(total_marks/n))
    
if __name__ == "__main__":
    main()


