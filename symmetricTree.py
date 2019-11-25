# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
 

# But the following [1,2,2,null,3,null,3] is not:

#     1
#    / \
#   2   2
#    \   \
#    3    3
 

# Note:
# Bonus points if you could solve it both recursively and iteratively.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.pre = []
        self.post = []
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        self.postOrder(root.left)
        self.preOrder(root.right)
        # print(self.post)
        # print(self.pre)
        return self.pre == self.post
       
    def postOrder(self,node):
        if node:
            if not node.left and not node.right:
                self.post.append(node.val)
            else:
                self.postOrder(node.right)
                self.postOrder(node.left)
                self.post.append(node.val)
                
        else:
            self.post.append(None)
    
    #Not in order but Left-Right-Root
    def preOrder(self,node):
        if node:
            if not node.left and not node.right:
                self.pre.append(node.val)
            else:
                self.preOrder(node.left)
                self.preOrder(node.right)
                self.pre.append(node.val)
                
        else:
            self.pre.append(None)
    
            