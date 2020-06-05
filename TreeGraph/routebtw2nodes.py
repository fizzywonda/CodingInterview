"""
Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.nbr = {}
        self.visited = False

    def getnbr(self):
        return [nbr for nbr in self.nbr.values()]

class Queue:
    def __init__(self):
        self.queue = []

    def dequeue(self):
        element = self.queue[0]
        del self.queue[0]
        return element

    def enqueue(self, element):
        self.queue.append(element)


def depth_first_search(graph, start, end):
    if start == end:
        return True
    start.visited = True
    for node in start.getnbr():
        if not node.visited:
            node.visited == True
            depth_first_search(node)


def breadth_first_search(graph, start, end):
    q = Queue()
    if start == end:
        return False
    start.visited = True
    q.enqueue(start)
    while len(q.queue) > 0:
        node = q.dequeue()
        for nbr in node.getnbr():
            if nbr == end:
                return True
            else:
                if not nbr.visited:
                    nbr.visited = True
                    q.enqueue(nbr)

    return False
