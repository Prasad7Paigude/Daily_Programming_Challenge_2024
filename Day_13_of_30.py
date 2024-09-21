"""
You are given a string s. Your task is to find and return the longest palindromic substring within the given string. A palindrome is a string that reads the same forwards and backwards.

Input:
A string s of length n. The length of the string satisfies 1≤n≤1000.

Output:
Return the longest substring of s that is a palindrome. If there are multiple solutions, return the first one that occurs.

Examples:
Example 1
Input: "babad"
Output: "bab"
Explanation: Both "bab" and "aba" are palindromic substrings, but since "bab" appears first in the string, it is returned.
"""
# Answer -
def longestPalindrome(s):
    n = len(s)
    if n == 0:
        return ""
    start = 0
    max_len = 1
    for i in range(1, n):
        low = i - 1
        high = i
        while low >= 0 and high < n and s[low] == s[high]:
            if high - low + 1 > max_len:
                start = low
                max_len = high - low + 1
            low -= 1
            high += 1
        low = i - 1
        high = i + 1
        while low >= 0 and high < n and s[low] == s[high]:
            if high - low + 1 > max_len:
                start = low
                max_len = high - low + 1
            low -= 1
            high += 1
    return s[start:start + max_len]

# Test cases -
print(longestPalindrome("babad"),"\n")
print(longestPalindrome("cbbd"),"\n")
print(longestPalindrome("a"),"\n")
print(longestPalindrome("aaaa"),"\n")
print(longestPalindrome("abc"))
