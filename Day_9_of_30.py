"""
Problem : Longest Common Prefix
You are given an array of strings strs[], consisting of lowercase letters. Your task is to find the longest common prefix shared among all the strings. If there is no common prefix, return an empty string "".

Input :
An array of strings strs[] where each string consists of lowercase English letters.
Example: strs[] = ["flower", "flow", "flight"]

Output :
* A string representing the longest common prefix. If no common prefix exists, return an empty string "".
Example: "fl"
"""
# Answer - 
def longestCommonPrefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for string in strs[1:]:
        while string[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return
    return prefix

# Test Case 1
strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs),"\n")

# Test Case 2
strs = ["dog", "racecar", "car"]
print(longestCommonPrefix(strs),"\n")

# Test Case 3
strs = ["apple", "ape", "april"]
print(longestCommonPrefix(strs),"\n")

# Test Case 4
strs = [""]
print(longestCommonPrefix(strs),"\n")

# Test Case 5
strs = ["alone"]
print(longestCommonPrefix(strs))
