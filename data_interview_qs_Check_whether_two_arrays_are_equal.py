# Check whether two arrays are equal

# Python Data Structures Arrays
# Given two arrays, write a function in vanilla Python (e.g., no libraries) to check whether or not the arrays are equal. You can consider the two arrays equal if both of them contain the same set of elements - the order of elements can differ.

# For example:

# #Given the following:
# arr1 = [1,5,6,7,8,0]
# arr2 = [0,5,7,6,8,1]

# #output = Yes
# arr3 = [1,5,6,7,8,0]
# arr4 = [0,7,7,7,8,1]

def arrays_are_equal(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    dict_arr = {}
    for i in arr1:
        if dict_arr.get(i):
            temp = dict_arr[i] + 1
            dict_arr[i] = temp
        else:
            dict_arr[i] = 1

    for i in arr2:
        if dict_arr.get(i):
            if dict_arr[i] - 1 <= 0:
                del dict_arr[i]
            else:
                temp = dict_arr[i] - 1
                dict_arr[i] = temp
        else:
            return False
    
    return True

arr1 = [1,5,6,7,8,0]
arr2 = [0,5,7,6,8,1]
arr3 = [1,5,6,7,8,0]
arr4 = [0,7,7,7,8,1]
arr5 = [1,2]
arr6 = [1,1,1,1]
arr7 = [1,1,1,1]
arr8 = [1,1,1]

print(arrays_are_equal(arr1, arr2)) #True
print(arrays_are_equal(arr3, arr4)) #False
print(arrays_are_equal(arr3, arr5)) #False
print(arrays_are_equal(arr5, arr4)) #False
print(arrays_are_equal(arr6, arr7)) #True
print(arrays_are_equal(arr6, arr8)) #False
print(arrays_are_equal(arr8, arr6)) #False
         