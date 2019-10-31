# Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

import copy
class Solution(object):
   
    def findPath(self, graph, u, v, path, visited):
        visited[u] = True
        path.append(u)
        if u == v:            
            output.append(copy.copy(path))
            
            
        else:
            for i in graph[u]:
                if not visited[i]:
                    self.findPath(graph,i,v,path,visited)
        
        
        visited [u] = False
        path.pop()
        
    
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        global output
        output = []
        visited = [False for i in range(len(graph))]
        path = []
        self.findPath(graph, 0, len(graph)-1, path, visited)
        return output
        