"""
Problem : Group Anagrams
You are given an array of strings strs[]. Your task is to group all the strings that are anagrams of each other. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input :
strs[] = ["eat", "tea", "tan", "ate", "nat", "bat"]

Output :
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
"""
# Answer -
from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)
    for string in strs:
        sorted_str = ''.join(sorted(string))
        anagram_map[sorted_str].append(string)
    return list(anagram_map.values())

# Test Case 1
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs),"\n")

# Test Case 2
strs =  [""]
print(groupAnagrams(strs),"\n")

# Test Case 3
strs = ["a"]
print(groupAnagrams(strs),"\n")

# Test Case 4
strs =  ["abc", "bca", "cab", "xyz", "zyx", "yxz"]
print(groupAnagrams(strs),"\n")

# Test Case 5
strs = ["abc", "def", "ghi"]
print(groupAnagrams(strs))

