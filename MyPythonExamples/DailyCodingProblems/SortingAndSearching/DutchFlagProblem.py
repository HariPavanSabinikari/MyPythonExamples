def partition_for_two(arr):
    low, high = 0, len(arr)-1
    while low <= high:
        if arr[low] == 'R':
            low +=1
        else:
            arr[low],arr[high] = arr[high],arr[low]
            high -= 1
    return arr

arr=['G','R','G','R']
print(partition_for_two(arr))

def partition_for_three(array):
    low,mid, high = 0, 0, len(array) -1
    while mid <= high:
        if array[mid] == 'R':
            array[low],array[mid] = array[mid],array[low]
            low += 1
            mid += 1
        elif array[mid] == 'G':
            mid +=1
        else:
            array[mid],array[high] = array[high],array[mid]
            high -= 1
    return array

array=['G','R','B','B','R','G']
print(partition_for_three(array))