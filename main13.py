L = [7,9,2,4,6,8,1,3,5,10]
print("Original list: ", L)

count = 0
for i in L:
    count += 1
print("sum: ", count)

avg = count/len(L)
print("Average: ",avg)

L.sort()
print("Smallest element is:", L[0])
print("largest element is:", L[-1])