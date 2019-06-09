def counting_sort(array,digit,base=10):
    print("hi how are you",digit)
    counts=[[] for _ in range(base)]
    print(counts)
    
    for num in array:
        print("array element",num)
        print("base ** digit",base ** digit)
        d=(num // base ** digit) % base
        print(d)
        counts[d].append(num)
        print("--each it",counts)
    
    print(counts)
    result=[]
    for bucket in counts:
        result.extend(bucket)
    print("---",result)  
    return result

def radix_sort(array,digits=3):
    for digit in range(digits):
        array = counting_sort(array, digit)
    return array

arr=[100,4,54,537,2,89,3]
print(radix_sort(arr))
        
    
    