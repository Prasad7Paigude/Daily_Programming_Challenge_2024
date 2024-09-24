"""
You are given two integers, N and M. Your task is to find the Least Common Multiple (LCM) of these two numbers. The LCM of two integers is the smallest positive integer that is divisible by both N and M.
Input:
Two integers N and M, where 1≤N,M≤109
Output:
A single integer representing the Least Common Multiple of N and M.
Examples:
Example 1
Input: N = 4, M = 6
Output: 12
Explanation: The smallest number divisible by both 4 and 6 is 12.
"""
# Answer -
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(N, M):
    return abs(N * M) // gcd(N, M)

# Test Cases -
print(lcm(4, 6))          
print(lcm(5, 10))         
print(lcm(7, 3))          
print(lcm(1, 987654321))  
print(lcm(123456, 789012)) 
