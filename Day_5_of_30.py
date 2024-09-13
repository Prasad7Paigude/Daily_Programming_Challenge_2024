"""
Problem : Find the Leaders in an Array
You are given an integer array arr of size n. An element is considered a leader if it is greater than all the elements to its right. Your task is to find all such leader elements in the array.

Input :
An integer array arr of size n.
Example : 
arr = [16, 17, 4, 3, 5, 2]

Output :
Return an array containing all the leader elements in the order in which they appear in the original array.
Example:
Leaders: [17, 5, 2]
"""
# Answer -
def find_leaders(arr):
    n = len(arr)
    leaders = []
    current_leader = arr[-1]
    leaders.append(current_leader)
    for i in range(n-2, -1, -1):
        if arr[i] > current_leader:
            current_leader = arr[i]
            leaders.append(current_leader)
    leaders.reverse()   
    return leaders

# Test Case 1
arr = [1, 2, 3, 4, 0]
print("Leaders:", find_leaders(arr),"\n")

# Test Case 2
arr = [7, 10, 4, 10, 6, 5, 2]
print("Leaders:", find_leaders(arr),"\n")

# Test Case 3
arr = [5]
print("Leaders:", find_leaders(arr),"\n")

# Test Case 4
arr = [100, 50, 20, 10]
print("Leaders:", find_leaders(arr),"\n")


