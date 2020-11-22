class Graph:

    # init function to declare class variables
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def BFSUtil(self, v, visited):
        temp = []
        queue = []
        visited[v] = True
        temp.append(v)
        queue.append(v)

        while queue:
            s = queue.pop(0)
            #print(s, end=" ")
            for i in self.adj[s]:
                if visited[i] == False:
                    queue.append(i)
                    temp.append(i)
                    visited[i] = True
        return temp

        # method to add an undirected edge

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

        # Method to retrieve connected components

    # in an undirected graph
    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                cc.append(self.BFSUtil(v, visited))
        return cc

# Driver Code
# Create a graph given in the above diagram
# 5 vertices numbered from 0 to 4
v = int(input("No. of vertices "))
e = int(input("No of edges "))
g = Graph(v)
for i in range(e):
    x = int(input())
    y = int(input())
    g.addEdge(x, y)
#g.addEdge(1, 0)
#g.addEdge(2, 3)
#g.addEdge(3, 4)
cc = g.connectedComponents()
print("Following are connected components")
print(cc)
