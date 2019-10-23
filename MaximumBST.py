# Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

# The root is the maximum number in the array.
# The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
# Construct the maximum tree by the given array and output the root node of this tree.

# Example 1:
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:

#       6
#     /   \
#    3     5
#     \    / 
#      2  0   
#        \
#         1
# Note:
# The size of the given array will be in the range [1,1000].


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        try:      
            num = max(nums)
            max_index = nums.index(num)
            # print(max_index)
            x = TreeNode(num)
            # print("node created",x)
            # print("left of node is", nums[0:max_index])
            # print("right of node is", nums[max_index+1:])
            x.left = self.constructMaximumBinaryTree(nums[0:max_index])
            
            x.right = self.constructMaximumBinaryTree(nums[max_index+1:])
            return x
        except ValueError:
            pass

     ###############################################################################################
     							#FAST SOLUTION

     ###############################################################################################

      def constructMaximumBinaryTree(self, nums):
            """
            :type nums: List[int]
            :rtype: TreeNode
            """
            myStack = []
            for n in nums:
                node = TreeNode(n)
                while myStack:
                    element = myStack[-1]
                    # print("element from stack is", element.val, "n is", n)
                    if element.val>n:
                        element.right = node
                        break
                    else:
                        element = myStack.pop(-1)
                        node.left=element
                        # myStack.append(node)
                myStack.append(node)
                # print("myStack is", myStack)
            return myStack[0]
            
                        


