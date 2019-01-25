print('Importing the fileone, the name variable is:', __name__)
def functionA():
    print('functionA is called')
def functionB():
    print('functionB is called')

if __name__ == '__main__':
    functionA()
    functionB()
else: print('fileone module is imported from another module')
