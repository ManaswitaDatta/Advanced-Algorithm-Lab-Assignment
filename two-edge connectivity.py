class Graph:

    # init function to declare class variables
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]
        self.Time = 0

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def bridgeUtil(self, u, visited, parent, low, disc):
        visited[u] = True
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1

        # Recur for all the vertices adjacent to this vertex
        for v in self.adj[u]:
            if not visited[v]:
                parent[v] = u
                if self.bridgeUtil(v, visited, parent, low, disc):
                    return True
                low[u] = min(low[u], low[v])

                ''' If the lowest vertex reachable from subtree 
                under v is below u in DFS tree, then u-v is 
                a bridge'''
                if low[v] > disc[u]:
                    return True

            # Update low value of u for parent function calls.
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def bridge(self):
        visited = [False] * self.V
        disc = [float("Inf")] * self.V
        low = [float("Inf")] * self.V
        parent = [-1] * self.V

        for i in range(self.V):
            if not visited[i]:
                if self.bridgeUtil(i, visited, parent, low, disc):
                    return True
        return False

# Driver Code
# Create a graph given in the above diagram
# 5 vertices numbered from 0 to 4
'''
v = int(input("No. of vertices "))
e = int(input("No of edges "))
g = Graph(v)
for i in range(e):
    x = int(input())
    y = int(input())
    g.addEdge(x, y)
'''
g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
g1.addEdge(0, 4) #remove this, then true
print("True") if g1.bridge() else print("False")