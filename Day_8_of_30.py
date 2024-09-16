"""
Problem : Reverse a String Word by Word
You are given a string s that consists of multiple words separated by spaces. Your task is to reverse the order of the words in the string. Words are defined as sequences of non-space characters. The output string should not contain leading or trailing spaces, and multiple spaces between words should be reduced to a single space.

Input :
A string s of length n (1 ≤ n ≤ 10^4) consisting of letters, digits, punctuation, and spaces.
Example : "the sky is blue"

Output :
* A string where the words in s are reversed, with a single space separating the words, and no leading or trailing spaces.
Example: "blue is sky the"
"""
# Answer - 
def reverse_words(s: str) -> str:
    words = s.split()
    reversed_words = words[::-1]
    result = ' '.join(reversed_words) 
    return result

# Test Case 1
reverse_words("the sky is blue")
print("Reversed Words:", reverse_words("the sky is blue"),"\n")

# Test Case 2
reverse_words("  hello world  ")
print("Reversed Words:", reverse_words("  hello world  "),"\n")

# Test Case 3
reverse_words("a good   example")
print("Reversed Words:", reverse_words("a good   example"),"\n")

# Test Case 4
reverse_words("    ")
print("Reversed Words:", reverse_words("    "),"\n")

# Test Case 5
reverse_words("word")
print("Reversed Words:", reverse_words("word"))


