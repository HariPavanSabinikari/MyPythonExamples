def max_pos(lst):
    return lst.index(max(lst))

def reverse(lst,i,j):
    while i<j:
        lst[i],lst[j]=lst[j],lst[i]
        i += 1
        j -= 1
    

def pancake_sor(lst,l=1,m=3):
    for size in reversed(range(len(lst))):
        max_ind = max_pos(lst[:size+1])
        reverse(lst,l,m)
        #reverse(lst,0,size)
    return lst

arr = [10,20,30,40,50]
print(pancake_sor(arr))