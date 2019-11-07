# Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

#  

class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        myStack = 0
        count = 0
        for p in S:
            if p == '(':
                myStack+=1
            else:
                if myStack>0:
                    myStack-=1
                else:
                    count+=1
        count+= myStack
        return count