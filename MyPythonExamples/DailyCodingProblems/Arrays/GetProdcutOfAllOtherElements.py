
def products(nums):
    #Generate Prefix products
    prefix_products = []
    for num in nums:
        print(num)
        print(prefix_products)
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)
    print(prefix_products)
    print("\n")
    
    #Generate suffix products
    suffix_products = []
    for num in reversed(nums):
        print(num)
        print(suffix_products)
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
        print(suffix_products)
    suffix_products=list(reversed(suffix_products))
    print(suffix_products)
    print("\n")
       
    #Generate result from the product of prefixes and suffixes.
    result=[]
    for i in range(len(nums)):
        if(i==0):
            result.append(suffix_products[i+1])
        elif i==len(nums) -1:
            result.append(prefix_products[i-1])
        else:
            result.append(prefix_products[i-1] * suffix_products[i+1])
    return result
        
             

nums=[1,2,3,4,5]
print(products(nums))