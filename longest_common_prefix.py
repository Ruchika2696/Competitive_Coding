# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # print(strs)
        if len(strs)==0:
            return ""
        count=""
        # temp = strs[0]
        for i in range(0,len(strs[0])):
            flag = True
            # print(i)
            
            for s in strs[1:]:
                try:
                    if strs[0][i] != s[i]:
                        flag = False
                        return count
                except IndexError:
                    flag=False
                    return count
                    
                    
  