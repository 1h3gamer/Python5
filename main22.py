def multiply_tuple(nums):
    temp=list(nums)
    product = 1
    for x in temp:
        product *= x
    return product

num = [3,6,7,5,4,1,2]
print("Original tuple", num)
print("Product of tuple", multiply_tuple(num))

num = [7,8,4,5,6,0,2]
print("Original tuple", num)
print("Product of tuple", multiply_tuple(num))