class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def addEdge(self, u, v):
        self.adj[u].append(v)  # directed graph

    def topologicalSortUtil(self, v, visited, stack):

        visited[v] = True
        for i in self.adj[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        stack.insert(0, v)


    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        print(stack)


v = int(input("No. of vertices "))
e = int(input("No of edges "))
g = Graph(v)
for i in range(e):
    x = int(input())
    y = int(input())
    g.addEdge(x, y)

# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)
print("Following is a Topological Sort of the given graph")
g.topologicalSort()