def main():
    '''This is a program to generate a cross product list from two lists'''
    names = ['Rahul','Priyanka','Ram','Sita','Pawan']
    marks = ['175','153','178','143','180']
    namemark = [[x,y] for x in names for y in marks ]
    print (namemark)
    

if __name__ == '__main__':
    main()
