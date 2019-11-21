# Given an undirected graph, return true if and only if it is bipartite.

# Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

# The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.



class Solution(object):
    
    def checkBipartite(self,graph, node):
        queue = []
        queue.append(node)
        if colors[node] == -1:
            colors[node] = 0
        
        while queue:
            u = queue.pop()
            if not visited[u]:
                visited[u] = True
                for edge in graph[u]:
                    if colors[edge] == -1:
                        queue.append(edge)
                        colors[edge] = 1 - colors[u]
                    if colors[edge] == colors[u]:
                        return False                                   
        return True
    
    
    
    
    
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        global visited, colors
        N = len(graph)
        if N == 0:
            return True
        colors = [-1 for i in range(N)]
        visited = [False for i in range(N)]        
        test = self.checkBipartite(graph, 0)
        if not test:
            return False
        for i in range(N):
            if not visited[i]:
                test = self.checkBipartite(graph, i)
                if not test:
                    return False
        return True     
        

