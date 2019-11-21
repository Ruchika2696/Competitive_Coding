# Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

 

# Example:



# Input:
# {"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

# Explanation:
# Node 1's value is 1, and it has two neighbors: Node 2 and 4.
# Node 2's value is 2, and it has two neighbors: Node 1 and 3.
# Node 3's value is 3, and it has two neighbors: Node 2 and 4.
# Node 4's value is 4, and it has two neighbors: Node 1 and 3.

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        myMap = {}
        queue = []
        
        newNode = Node(node.val, [])
        queue.append(node)
        myMap[node] = newNode
        
        while(queue):
            popped_node = queue.pop()
            
            for neighbor in popped_node.neighbors:
                if neighbor not in myMap:
                    queue.append(neighbor)
                    newNode = Node(neighbor.val, [])
                    myMap[neighbor] = newNode
                    myMap[popped_node].neighbors.append(newNode)
                else:
                    myMap[popped_node].neighbors.append(myMap[neighbor])
        
        return myMap[node]
                    
                    
                
                
        