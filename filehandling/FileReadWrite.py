import sys
sys.path.append('/Users/rahuljain/Desktop/Python/PythonPrograms/filehandling')
def generatesalary(file1,file2,file3):
    mast = open(file1,'r')
    hour = open(file2,'r')
    targ = open(file3,'w')
    targ.write('empid_m,name,rate,hours,salary' + '\n')
    mast_line = mast.readline()
    hour_line = hour.readline()
    
    while(mast_line != ''  and hour_line != ''):
        mast_list = mast_line.split(',')
        hour_list = hour_line.split(',')

        empid_m  = int(mast_list[0])
        name     = mast_list[1]
        rate     = int(mast_line[2])
        empid_h  = int(hour_list[0])
        hours    = int(hour_line[1])
        print(empid_m,name,rate,empid_h,hours)
        
        if empid_m == empid_h:
            salary = rate * hours
        
        targ.write(str(empid_m) + ',' + name + ',' + str(rate) + ',' + str(hours) + ',' + str(salary) + '\n')
        
        mast_line = mast.readline()
        hour_line = hour.readline()
    
    mast.close()
    hour.close()
    targ.close()

def main():
    file1 = 'master'
    file2 = 'hours'
    file3 = 'salary'
    generatesalary(file1,file2,file3)

if __name__ == '__main__':
    main()
