import matplotlib.pyplot as plt

def plotfunction(a,b,step):
    nsteps = int((b-a)/step)
    x = [a+step*i for i in range(nsteps+1)]
    y1 = [t**2 for t in x]
    y2 = [t**3 for t in x]
    plt.plot(x,y1,'ro--',label = 'x vs x**2')
    plt.plot(x,y2,'r<-.',label = 'x vs x**3')
    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('x vs x**2 and x vs x**3')
    plt.grid()
    plt.show()
    

def main():
    a = float(input('Enter the first element of the range :'))
    b = float(input('Enter the last element of the range :'))
    step = float(input('Enter the step size'))
    plotfunction(a,b,step)
    
    
if __name__ == '__main__':
    main()
