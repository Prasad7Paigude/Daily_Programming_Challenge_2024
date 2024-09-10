""".
Problem: Find the missing number
You are given an array arr containing n-1 distinct integers. The array consists of integers taken from the range 1 to n, meaning one integer is missing from this sequence. Your task is to find the missing integer.

Input :
An integer array arr of size n-1 where the elements are distinct and taken from the range 1 to n.
Example : arr = [1, 2, 4, 5]

Output :
Return the missing integer from the array.
Example: Missing Number : 3
"""
# Answer - 
def find_missing_no_from_array(arr):
    n = len(arr) + 1
    exp_sum = n * (n + 1) // 2
    act_sum = sum(arr)
    miss_no = exp_sum - act_sum
    return miss_no

# Test Case 1
arr = [1, 2, 4, 5]
answer = find_missing_no_from_array(arr)
print("Missing number : ", answer, "\n")

# Test Case 2
arr = [2, 3, 4, 5]
answer = find_missing_no_from_array(arr)
print("Missing number : ", answer, "\n")

# Test Case 3
arr = [1, 2, 3, 4]
answer = find_missing_no_from_array(arr)
print("Missing number : ", answer, "\n")

# Test Case 4
arr = [1]
answer = find_missing_no_from_array(arr)
print("Missing number : ", answer, "\n")

# Test Case 5
arr = list(range(1, 1000000))
answer = find_missing_no_from_array(arr)
print("Missing number : ", answer, "\n")
