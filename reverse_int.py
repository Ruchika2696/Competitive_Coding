# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.



class Solution:

    def reverse(self, x: int) -> int:
        if x>0:
            ans = int(str(x)[::-1])
        if x<0:
            ans = str(x)[1:]
            ans = - int(str(ans)[::-1])
        elif x==0:
            return 0
        
        if ans>2147483648 or ans<-2147483648:
            return 0
        else:
            return ans
      