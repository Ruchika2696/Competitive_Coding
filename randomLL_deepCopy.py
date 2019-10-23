# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

# Return a deep copy of the list.


##MY SOL: Create a hashmap to map original node and copy node in first iteration. In second iteration, put the wires at right place
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        n = head
        myDict = {}
        while n != None:
            # print(n.val)
            myDict[n] = Node(n.val, None, None)
            n = n.next
            
        
        # for key in myDict:
        #     print(myDict[key].val)
            
        n = head
        while n!=None:
            nextPt = n.next
            ranPt = n.random
            if nextPt != None:
                myDict[n].next = myDict[nextPt]
            if ranPt!=None:
                myDict[n].random = myDict[ranPt]
            
            n = n.next
        if head!=None:
            return myDict[head]

            
#####################################################################################################
						#APPROACH 2        
#####################################################################################################

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head!=None:
            n = head

           	#set next pointer of original node to its copy
            while n!=None:
                copyNode = Node(n.val, n.next, None)
                n.next = copyNode
                n = n.next.next

            #wire random pointers of copy nodes to original node's random
            n=head
            while n!=None:
                if n.random != None:
                    n.next.random = n.random.next
                else:
                    n.next.random = None
                n = n.next.next


            #set next pointers of copy nodes and original nodes
            original_head = head
            if original_head.next!=None:
                new_head = original_head.next
                x = new_head
                while new_head!=None:
                    if original_head.next!=None:
                        if new_head.next!=None:
                            original_head.next = new_head.next
                            new_head.next = original_head.next.next
                        else:
                            original_head.next = None

                    new_head = new_head.next
                return x 
