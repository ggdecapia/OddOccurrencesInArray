def solution(A):
    # write your code in Python 3.6
    # sort given array in ascending order
    sorted_array = sorted(A)
    # get the array length to determine the for-loop reange
    array_len = len(sorted_array)
    # iterate through the sorted elements starting with index 1
    for i in range(1,array_len,2): # step 2 is used to read each pair
        #print(i)
        #print(sorted_array[i])
        if sorted_array[i] == sorted_array[i-1]:
            odd_num = sorted_array[i+1]
        else:
            return(sorted_array[i-1])
    return(sorted_array[array_len-1])