# For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

# Format
# The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# Example 1 :

# Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

#         0
#         |
#         1
#        / \
#       2   3 

# Output: [1]
# Example 2 :

# Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

#      0  1  2
#       \ | /
#         3
#         |
#         4
#         |
#         5 

# Output: [3, 4]
# Note:

# According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.


from Queue import Queue
class Solution(object):      
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 0:
            return []
        if n == 1:
            return [0]
        
        if n == 2:
            return [0,1]

        tree = {}
        degree = [0 for i in range(n)]
        vertex = [0 for i in range(n)]

        for edge in edges:
            degree[edge[0]]+=1
            degree[edge[1]]+=1
            if edge[0] not in tree:
                tree[edge[0]] = [edge[1]]
            else:
                tree[edge[0]].append(edge[1])
            
            if edge[1] not in tree:
                tree[edge[1]] = [edge[0]]
            else:
                tree[edge[1]].append(edge[0])
      
        q = []
        
        for i,d in enumerate(degree):
            if d == 1:
                q.append(i)
       
        
        while len(tree)>2:
            for i in range(len(q)):
                leaf = q.pop(0)
                for neighbor in tree[leaf]:
                    degree[neighbor] -=1
                    tree[neighbor].remove(leaf)
                    if degree[neighbor] == 1:
                        q.append(neighbor)

                del tree[leaf]
               
        return tree.keys()
        
