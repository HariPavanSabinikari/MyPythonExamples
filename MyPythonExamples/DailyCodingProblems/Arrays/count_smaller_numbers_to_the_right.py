import bisect
#O(n^2)
def count_smaller_number(lst):
    result=[]
    
    for i, num in enumerate(lst):
        count=sum(val < num for val in lst[i+1:])
        result.append(count)
    return result

def count_smaller_efficiently(lst):
    result=[]
    seen=[]
    
    for num in reversed(lst):
        i= bisect.bisect_left(seen,num)
        result.append(i)
        bisect.insort(seen, num)
    return list(reversed(result))

a=[3,4,9,6,1]
print(count_smaller_number(a))
print(count_smaller_efficiently(a))