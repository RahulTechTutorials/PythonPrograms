import matplotlib.pyplot as plt

def square(x,y):
    plt.plot(x,y,'ro--')

def main():
    size = int(input('Enter the size of the square:'))
    x = [0,size,size,0,0]
    y = [0,0,size,size,0]
    square(x,y)
    plt.title('square')
    plt.axis([min(x)-1,max(x)+1,min(y)-1,max(y)+1])
    plt.grid()
    plt.show()
if __name__ == '__main__':
    main()
