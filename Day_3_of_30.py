"""
You are given an array arr containing n+1 integers, where each integer is in the range [1, n] inclusive. There is exactly one duplicate number in the array, but it may appear more than once. Your task is to find the duplicate number without modifying the array and using constant extra space.

Input:
An integer array arr of size n+1, where each element is an integer in the range [1, n].
Example : arr = [3, 1, 3, 4, 2]

Output:
Return the duplicate integer present in the array.
Example: Duplicate number: 3
"""
# Answer -
def findDuplicate(arr):
    i = arr[0]
    j = arr[0]
    while True:
        i = arr[i]
        j = arr[arr[j]]
        if i == j:
            break
    i = arr[0]
    while i != j:
        i = arr[i]
        j = arr[j]
    return i

# Test case 1
arr = [1, 3, 4, 2, 2]
duplicate = findDuplicate(arr)
print(f"Duplicate number: {duplicate}")

# Test case 2
arr = [3, 1, 3, 4, 2]
duplicate = findDuplicate(arr)
print(f"Duplicate number: {duplicate}")

# Test case 3
arr = [1, 1]
duplicate = findDuplicate(arr)
print(f"Duplicate number: {duplicate}")

# Test case 4
arr = [1, 4, 4, 2, 3]
duplicate = findDuplicate(arr)
print(f"Duplicate number: {duplicate}")

