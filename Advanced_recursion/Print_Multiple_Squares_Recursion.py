import matplotlib.pyplot as plt

def square(x,y):
    if (x[1] - x[0]) >= 1:
        plt.plot(x,y,'ro--')
        x = [x[0]+1,x[1]-1,x[2]-1,x[3]+1,x[4]+1]
        y = [y[0]+1,y[1]+1,y[2]-1,y[3]-1,y[4]+1]
        square(x,y)

def wrapperFunction(size):
    x = [0,size,size,0,0]
    y = [0,0,size,size,0]
    square(x,y)
    plt.title('square')
    plt.axis([min(x)-1,max(x)+1,min(y)-1,max(y)+1])
    plt.grid()
    plt.show()
    
        
def main():
    size = int(input('Enter the size of the square:'))
    wrapperFunction(size)
    
    
if __name__ == '__main__':
    main()
