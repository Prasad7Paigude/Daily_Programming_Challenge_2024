"""
You are given two sorted arrays arr1 of size m and arr2 of size n. Your task is to merge these two arrays into a single sorted array without using any extra space (i.e., in-place merging). The elements in arr1 should be merged first, followed by the elements of arr2, resulting in both arrays being sorted after the merge.

Input:
Two sorted integer arrays arr1 of size m and arr2 of size n.
Example : 
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

Output:
Both arr1 and arr2 should be sorted after the merge. Since you cannot use extra space, the final result will be reflected in arr1 and arr2.
Example:
arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]
"""
# Answer - 
def merge(arr1, arr2):
    m, n = len(arr1), len(arr2)
    for i in range(m):
        if arr1[i] > arr2[0]:
            arr1[i], arr2[0] = arr2[0], arr1[i]
            first = arr2[0]
            k = 1
            while k < n and arr2[k] < first:
                arr2[k - 1] = arr2[k]
                k += 1
            arr2[k - 1] = first


# Test Case 1
arr1 = [1, 3, 5] 
arr2 = [2, 4, 6]
merge(arr1, arr2)
print("arr1:", arr1)
print("arr2:", arr2,"\n")

# Test Case 2
arr1 = [10, 12, 14]
arr2 = [1, 3, 5]
merge(arr1, arr2)
print("arr1:", arr1)
print("arr2:", arr2,"\n")

# Test Case 3
arr1 = [2, 3, 8]
arr2 = [4, 6, 10]
merge(arr1, arr2)
print("arr1:", arr1)
print("arr2:", arr2,"\n")

# Test Case 4
arr1 = [1]
arr2 = [2]
merge(arr1, arr2)
print("arr1:", arr1)
print("arr2:", arr2,"\n")


