"""
You are given an integer array arr of size n. Your task is to find all the subarrays whose elements sum up to zero. A subarray is defined as a contiguous part of the array, and you must return the starting and ending indices of each subarray.

Input:
An integer array arr of size n where n represents the number of elements in the array.
Example : 
Input: [1, 2, -3, 3, -1, 2]

Output:
Return a list of tuples, where each tuple contains two integers. The starting index (0-based) of the subarray. The ending index (0-based) of the subarray.
The output should list all subarrays that sum to zero. If no such subarrays are found, return an empty list.
Example
Output: [(0, 2), (1, 3)]
"""
# Answer - 
def find_zero_sum_subarrays(arr):
    prefix_sum_map = {}
    prefix_sum = 0
    result = []
    for i in range(len(arr)):
        prefix_sum += arr[i]
        if prefix_sum == 0:
            result.append((0, i))
        if prefix_sum in prefix_sum_map:
            for start_index in prefix_sum_map[prefix_sum]:
                result.append((start_index + 1, i))
        if prefix_sum in prefix_sum_map:
            prefix_sum_map[prefix_sum].append(i)
        else:
            prefix_sum_map[prefix_sum] = [i]
    return result

# Test Case 1
arr =  [4, -1, -3, 1, 2, -1]
print(find_zero_sum_subarrays(arr),"\n")

# Test Case 2
arr =  [1, 2, 3, 4]
print(find_zero_sum_subarrays(arr),"\n")

# Test Case 3
arr =  [0, 0, 0]
print(find_zero_sum_subarrays(arr),"\n")

# Test Case 4
arr =  [-3, 1, 2, -3, 4, 0]
print(find_zero_sum_subarrays(arr))
