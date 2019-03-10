
def sumup(k,lst):
    length = len(lst)
    output = []
    for i in range(length-1):
        for j in range(i+1,length):
            if lst[i]+lst[j] ==k:
                output.append((lst[i],lst[j]))
            else :
                continue
    return output

if __name__ == '__main__':
    k = int(input('Enter the sum to be found'))
    lst = [1,3,2,5,46,6,7,4,6,3,9,5]
    out = sumup(k,lst)
    print(out)
            
        
