# Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the sum of the values of the original tree that are greater than or equal to node.val.

# As a reminder, a binary search tree is a tree that satisfies these constraints:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:



# Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
 

# Note:

# The number of nodes in the tree is between 1 and 100.
# Each node will have value between 0 and 100.
# The given tree is a binary search tree.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.NodeSum = [0]
        self.index=0
        
    def constructTree(self, root):
        if root:
            self.constructTree(root.left)
            # print("prev val=", root.val)
            root.val = self.NodeSum[-1]-self.NodeSum[self.index]
            # print("new val=", root.val)
            self.index+=1
            self.constructTree(root.right)
        
    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            # print(root)
            self.NodeSum.append(self.NodeSum[-1]+root.val)
            self.inOrder(root.right)
    
   
                
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.inOrder(root)
        self.constructTree(root)
        # print(self.NodeSum)
        return root
        
