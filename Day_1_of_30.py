"""
Problem: Sort an Array of 0s, 1s, and 2s
You are given an array arr consisting only of 0s, 1s, and 2s. The task is to sort the array in increasing order in linear time (i.e., O(n)) without using any extra space. This means you need to rearrange the array in-place.

Input :
An integer array arr of size n where each element is either 0, 1, or 2.
Example : arr = [0, 1, 2, 1, 0, 2, 1, 0]

Output :
The sorted array, arranged in increasing order of 0s, 1s, and 2s.
Example: [0, 0, 0, 1, 1, 1, 2, 2]
"""
# Answer -
def sort(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

# Test Case 1
arr = [0, 1, 2, 1, 0, 2, 1, 0]
sorted_arr = sort(arr)
print(sorted_arr, "\n")

# Test Case 2
arr = [2, 2, 2, 2]
sorted_arr = sort(arr)
print(sorted_arr, "\n")

# Test Case 3
arr = [0, 0, 0, 0]
sorted_arr = sort(arr)
print(sorted_arr, "\n")

# Test Case 4
arr = [1, 1, 1, 1]
sorted_arr = sort(arr)
print(sorted_arr, "\n")

# Test Case 5
arr = [2, 0, 1]
sorted_arr = sort(arr)
print(sorted_arr, "\n")

# Test Case 6
arr = []
sorted_arr = sort(arr)
print(sorted_arr, "\n")