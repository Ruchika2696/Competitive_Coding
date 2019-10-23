# Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

# Two trees are duplicate if they have the same structure with same node values.

# Example 1:

#         1
#        / \
#       2   3
#      /   / \
#     4   2   4
#        /
#       4
# The following are two duplicate subtrees:

#       2
#      /
#     4
# and

#     4
# Therefore, you need to return above trees' root in the form of a list.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        dic=collections.defaultdict(list)
        # dic= {}
        def inOrder(root: TreeNode):
            if root: 
                strings = str(root.val) + inOrder(root.left) + inOrder(root.right)
                dic[strings].append(root)
                # if strings in dic:
                #     dic[strings].append(root)
                # # else:
                #     dic[strings] = [root]
                return strings
            else:
                return ' '
        # print(root)
        ans=[]
        x = inOrder(root)
        # print(x)
        # print(dic)
        for key in dic:
            if len(dic[key])>1:
                ans.append(dic[key][0])
        return (ans)
        