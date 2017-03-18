'''
Given a undirected graph, a node and a target, return the
nearest node to given node which value of it is target, return
NUll if cannot find.


'''
import Queue

class Solution:

    # @param graph, a list of undirected graph node
    # @param values, a dict
    # @param node ,an undirected grapn node
    # @param target,, a target node

    def searchNode(self, graph, values, node, target):
        q = Queue.Queue(maxsize = len(graph))
        if values[node] = target:
            return node

        q.put(node)
        del values[node]

        while not q.empty():
            head = q.get()
            for n in head.neighbors:
                if n in values:
                    if values[n] == target:
                        return n
                    del values[n]
                    q.put(n)
        return None
