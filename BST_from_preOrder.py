#  	Return the root node of a binary search tree that matches the given preorder traversal.

# (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

 

# Example 1:

# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]

 

# Note: 

# 1 <= preorder.length <= 100
# The values of preorder are distinct.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def constructTree(self, preorder, minVal, maxVal):
        root = None
        if len(preorder)>0: 
            val = preorder[0]

            if val>minVal and val<maxVal:
                root = TreeNode(val)
                preorder.remove(val)
           
                if len(preorder)>0:
                    root.left = self.constructTree(preorder, minVal, root.val)
                    root.right = self.constructTree(preorder, root.val, maxVal)
        
        return root
             
             
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        tree = self.constructTree(preorder,float('-inf'), float('inf'))
        return tree
        
        
