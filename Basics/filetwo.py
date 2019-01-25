import sys
sys.path.append('/Users/rahuljain/Desktop/Python/PythonPrograms/Basics')
import fileone
print('Called filetwo module, the name variable is:', __name__)
def functionC():
    print('functionC is called')
def functionD():
    print('functionD is called')

if __name__ == '__main__':
    functionC()
    functionD()
else: print('filetwo module is imported from another module')
