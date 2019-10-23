# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        # Check for empty string
        if s == "":
            return True
        # Check for odd length
        if len(s)%2!=0:
            return False
        myStack = []
        dic = {")":"(", "}":"{", "]":"["}
        for c in s:
            if c not in dic:
                myStack.append(c)
            elif myStack == [] or myStack.pop()!= dic[c]:
                return False         
        if myStack:
            return False
        else:
            return True