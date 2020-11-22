from collections import defaultdict


# This class represents a directed graph using
# adjacency list representation
class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def addEdge(self, u, v):
        self.adj[u].append(v) #directed graph

    def DFSUtil(self, s, visited, arrival, departure, parent):
        global Time
        arrival[s] = Time
        Time = Time + 1
        visited[s] = True
        print(s, end=" ")
        for u in self.adj[s]:
            if visited[u] == False:
                parent[u] = s
                self.DFSUtil(u, visited, arrival, departure, parent)
        departure[s] = Time
        Time = Time + 1

    # recursive DFSUtil()
    def DFS(self, s):
        visited = []
        arrival = [0]*self.V
        departure = [0]*self.V
        parent = [-1]*self.V
        for i in range(self.V):
            visited.append(False)
        parent[s] = -1
        self.DFSUtil(s, visited, arrival, departure, parent)
        for i in range(self.V):
            if visited[i] == False:
                parent[i] = -1
                self.DFSUtil(i, visited, arrival, departure, parent)

        return arrival, departure, parent

v = 9 #int(input("No. of vertices "))
e = 13 #int(input("No of edges "))
g = Graph(v)
edge = [[1, 2], [1, 5], [2, 3], [5, 6], [3, 7], [3, 4], [4, 8], [1, 4], [3, 8], [4, 2], [6, 1], [6, 7], [7, 8]]
list = []
for i in range(e):
    x = edge[i][0] #int(input())
    y = edge[i][1] #int(input())
    temp = []
    temp.append(x)
    temp.append(y)
    list.append(temp)
    g.addEdge(x, y)
s = int(input("Source vertex: "))
#g.addEdge(0, 1)
#g.addEdge(0, 2)
#g.addEdge(1, 2)
#g.addEdge(2, 0)
#g.addEdge(2, 3)
#g.addEdge(3, 3)
Time = 0
print("Following is DFS from (starting from vertex 2)")
arrival, departure, parent = g.DFS(s)
print("\n")
print("Arrival Time: ")
for x in range(v):
    print(arrival[x], end = " ")
print("\nDeparture Time: ")
for x in range(v):
    print(departure[x], end=" ")
tree = []
back = []
forward = []
cross = []
for x in list:
    i = x[0]
    j = x[1]
    if parent[j] == i:
        tree.append(x)
    elif arrival[j] <= arrival[i] and departure[i] <= departure[j]:
        back.append(x)
    elif arrival[i] > departure[j]:
        cross.append(x)
    else:
        forward.append(x)

print("\nTree Edge: ")
print(tree)
print("\nBack Edge: ")
print(back)
print("\nForward Edge: ")
print(forward)
print("\nCross Edge: ")
print(cross)