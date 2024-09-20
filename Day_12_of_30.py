"""
You are given a string s consisting of different types of parentheses: (), {}, and []. Your task is to determine whether the given string is valid.
A string is considered valid if:
Every opening bracket has a corresponding closing bracket of the same type.
The brackets are closed in the correct order. This means that a closing bracket must close the most recent unmatched opening bracket.

Input:
A string s consisting of characters (, ), {, }, [, and ].

Output:
Return true if the string is valid.
Return false if the string is invalid.

Examples:
Example 1
Input: s = "()"
Output: true
Explanation: The string contains only one pair of valid parentheses.
"""
# Answer -

def isValid(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False 
        else:
            stack.append(char)
    return not stack  

# Test Case 1
print(isValid("()"),"\n")

# Test Case 2       
print(isValid("([)]"),"\n")

# Test Case 3  
print(isValid("[{()}]"),"\n") 

# Test Case 4   
print(isValid(""),"\n")
  
# Test Case 5 
print(isValid("{[}"))   
