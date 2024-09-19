"""
You are given a string s. Your task is to generate and return all possible permutations of the characters in the string. A permutation is a rearrangement of the characters in the string, and each character must appear exactly once in every permutation. If there are duplicate characters in the string, the resulting permutations should also be unique (i.e., no repeated permutations).

Input:
A string s consisting of lowercase English letters. The length of the string n satisfies 1≤𝑛≤9.

Output:
An array of strings containing all unique permutations of the input string. The order of permutations in the output does not matter.

Examples:
Example 1
Input: "abc"
Output: ["abc", "acb", "bac", "bca", "cab", "cba"]
Explanation: All possible arrangements of "abc" are listed, and there are no duplicate permutations.
"""
# Answer -
def permute(s):
    def backtrack(current_permutation, used_characters):
        if len(current_permutation) == len(s):
            result.add(''.join(current_permutation))
            return
        for i in range(len(s)):
            if used_characters[i]:
                continue
            used_characters[i] = True
            current_permutation.append(s[i])
            backtrack(current_permutation, used_characters)
            current_permutation.pop()
            used_characters[i] = False
    result = set()
    used_characters = [False] * len(s)
    backtrack([], used_characters)
    return list(result)

# Test Case 1
s = "abc"
permutations = permute(s)
print(permutations,"\n")

# Test Case 2
s = "aab"
permutations = permute(s)
print(permutations,"\n")

# Test Case 1
s = "aaa"
permutations = permute(s)
print(permutations,"\n")

# Test Case 1
s = "a"
permutations = permute(s)
print(permutations,"\n")

# Test Case 1
s = "abcd"
permutations = permute(s)
print(permutations)
