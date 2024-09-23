"""
You are given a string S, and your task is to find the length of the longest substring that contains no repeating characters. A substring is a contiguous block of characters in the string.
In this problem, you need to find the length of the longest substring where all the characters are unique. The substring can be formed by starting at any position in the string, but it must not contain any repeated characters.

Input:
A string S, where 1≤∣S∣≤105(length of string).

Output:
An integer representing the length of the longest substring without repeating characters.

Examples:
Example 1
Input: S = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with a length of 3. Even though the string contains repeated characters, the longest substring without duplicates is "abc".
"""
# Answer -
def lengthOfLongestSubstring(s):
    n = len(s)
    seen = {}
    max_len = 0
    left = 0
    for right in range(n):
        if s[right] in seen and seen[s[right]] >= left:
            left = seen[s[right]] + 1
        seen[s[right]] = right
        max_len = max(max_len, right - left + 1)
    return max_len

# Test Cases -
print(lengthOfLongestSubstring("abcabcbb"),"\n")
print(lengthOfLongestSubstring("bbbbb"),"\n")
print(lengthOfLongestSubstring("pwwkew"),"\n")
print(lengthOfLongestSubstring("abcdefgh"),"\n")
print(lengthOfLongestSubstring("a"))

