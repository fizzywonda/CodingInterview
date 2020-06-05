"""
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
"""
from TreeGraph.MinimalTree import Node
from TreeGraph.routebtw2nodes import Queue

class LinkedList:
    def __init__(self):
        self.head = Node1(None)

    def add_node(self, node):
        if self.head is None:
            self.head = node
        else:
            self.head.next = node
            node = self.head


class Node1(Node):
    def __init__(self,data):
        super.__init__(data)
        self.visited = False
        self.next = None

def list_of_depth(start_node):
    q = Queue()
    start_node.visit = True
    q.enqueue(start_node)
    level = {}
    level[0]= start_node

    lvl = 0
    while len(q.queue) != 0:
        lvl += 1
        node = q.dequeue()
        lklst = LinkedList()
        for i in node.get_children():
            if i.visited != True:
                i.visited = True
                q.enqueue(i)
                lklst.add_node(i)
        level[lvl + 1] = lklst
