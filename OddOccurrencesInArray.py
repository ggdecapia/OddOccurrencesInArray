# sort given array in ascending order
sorted_array = sorted(A)
# get the array length to determine the for-loop reange
array_len = len(sorted_array)
# iterate through the sorted elements starting with index 1
for i in range(1,array_len,2): # step 2 is used to read each pair
    # if current element is equal to the previous, they are a pair
    if sorted_array[i] == sorted_array[i-1]:
        odd_num = sorted_array[i+1]
    # if current element is NOT equal to the previous, then the previous is the odd number
    else:
        print(sorted_array[i-1])
        break
# return the last element as the odd number
print(sorted_array[array_len-1])