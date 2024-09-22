"""
You are given a string s of lowercase English alphabets and an integer k. Your task is to count all possible substrings of s that contain exactly k distinct characters.

Input:
A string s consisting of lowercase English letters.
An integer k, where 1 ≤ 𝑘 ≤ 26
The length of the string satisfies 1 ≤ 𝑛 ≤ 104

Output:
Return an integer that represents the number of substrings of s that contain exactly k distinct characters.
"""
# Answer -
def countKDistinct(s, k):
    n = len(s)
    freq = {}
    left = 0
    count = 0
    distinct = 0
    for right in range(n):
        if s[right] not in freq or freq[s[right]] == 0:
            distinct += 1
        freq[s[right]] = freq.get(s[right], 0) + 1
        while distinct > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                distinct -= 1
            left += 1
        count += right - left + 1
    def atMostK(s, k):
        n = len(s)
        freq = {}
        left = 0
        count = 0
        distinct = 0
        for right in range(n):
            if s[right] not in freq or freq[s[right]] == 0:
                distinct += 1
            freq[s[right]] = freq.get(s[right], 0) + 1
            while distinct > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    distinct -= 1
                left += 1
            count += right - left + 1
        return count
    return atMostK(s, k) - atMostK(s, k - 1)

# Test cases -
print(countKDistinct("pqpqs", 2),"\n")
print(countKDistinct("aabacbebebe", 3),"\n")
print(countKDistinct("a", 1),"\n")
print(countKDistinct("abc", 3),"\n")
print(countKDistinct("abc", 2))
