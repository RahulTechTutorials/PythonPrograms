
def sumup(k,lst):
    length = len(lst)
    output = []
    lst = sorted(lst)
    i = 0
    j = -1
    
    while (lst[i] != lst[j]):
        if  lst[i]+lst[j] == k: 
            output.append((lst[i],lst[j]))
            i += 1
            j -= 1
        elif lst[i]+lst[j] > k:
            j -= 1
            continue

    return output

if __name__ == '__main__':
    k = int(input('Enter the sum to be found'))
    lst = [1,3,2,5,46,6,7,4,6,3,9,5]
    out = sumup(k,lst)
    print(out)
            
