from collections import defaultdict


# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize
        # next as null


# Linked List class
class LinkedList:

    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None
        self.tail = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end = ',')
            temp = temp.next
        print()
class Graph:

    def __init__(self, num_of_v):
        self.num_of_v = num_of_v
        self.edges = defaultdict(list)

    # graph is represented as an
    # array of edges
    def add_edge(self, u, v):
        self.edges[u].append(v)


class Subset:
    def __init__(self, value, parent, rank):
        self.parent = parent
        self.rank = rank
        self.value = value
        self.list = LinkedList()
        self.list.head = Node(value)
        self.list.tail = self.list.head

    # A utility function to find set of an element
# node(uses path compression technique)


def find(subsets, node):
    if subsets[node].parent != node:
        subsets[node].parent = find(subsets, subsets[node].parent)
    return subsets[node].parent


# A function that does union of two sets
# of u and v(uses union by rank)


def union(subsets, u, v):
    # Attach smaller rank tree under root
    # of high rank tree(Union by Rank)
    if subsets[u].rank > subsets[v].rank:
        subsets[v].parent = u
        subsets[u].list.tail.next = subsets[v].list.head
        subsets[u].list.tail = subsets[v].list.tail
    elif subsets[v].rank > subsets[u].rank:
        subsets[u].parent = v
        subsets[v].list.tail.next = subsets[u].list.head
        subsets[v].list.tail = subsets[u].list.tail
    # If ranks are same, then make one as
    # root and increment its rank by one
    else:
        subsets[v].parent = u
        subsets[u].rank += 1
        subsets[u].list.tail.next = subsets[v].list.head
        subsets[u].list.tail = subsets[v].list.tail
# The main function to check whether a given
# graph contains cycle or not


def printSet(graph):
    # Allocate memory for creating sets
    subsets = []

    for u in range(graph.num_of_v):
        subsets.append(Subset(u, u, 0))

    # Iterate through all edges of graph,
    # find sets of both vertices of every
    # edge, if sets are same, then there
    # is cycle in graph.
    for u in graph.edges:
        u_rep = find(subsets, u)

        for v in graph.edges[u]:
            v_rep = find(subsets, v)

            if u_rep != v_rep:
                union(subsets, u_rep, v_rep)

    for u in range(graph.num_of_v):
        v_rep = find(subsets, u)
        subsets[v_rep].list.printList()


# Driver code

# Create a graph given in
# the above diagram

v = int(input("No. of vertices "))
e = int(input("No of edges "))
g = Graph(v)
"""
for i in range(e):
    x = int(input())
    y = int(input())
    g.add_edge(x, y)
"""

g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
printSet(g)