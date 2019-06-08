from test._mock_backport import right


def window(array):
    left, right = None, None
    s = sorted(array)
    
    for i in range(len(array)):
        if s[i] != array[i] and left is None:
            left =i
        elif s[i] != array[i]:
            right = i
    return left,right

def window_efficiently(arr):
    left, right = None, None
    n=len(arr)
    max_seen, min_seen=-float("inf"), float("inf")
    
    for i in range(n):
        max_seen=max(max_seen,arr[i])
        if arr[i] < max_seen:
            right = i
            
    for i in range(n-1,-1,-1):
        min_seen=min(min_seen,arr[i])
        if arr[i] > min_seen:
            left = i
    return left,right

a=[3,7,5,6,9]
print(window(a))
print(window_efficiently(a))