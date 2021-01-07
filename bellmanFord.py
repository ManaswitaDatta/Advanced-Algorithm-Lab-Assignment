# number of nodes in the graph
print('Enter number of vertices in the graph:- ')
n = int(input())

# number of edges in the graph
print('Enter number of edges in the graph:- ')
m = int(input())

# graph to contain weighted edges
graph = []

print('Enter weighted edges of the graph')
for i in range(m):
    u, v, w = list(map(int, input().split()))
    graph.append([u, v, w])


def BellmanFord(src):
    # Initializing distance from source vertex to all vertices as INFINITE and distance of source vertex as 0
    list = [[float("inf") for i in range(n)] for j in range(n)]
    dist = [float("inf") for i in range(n)]
    dist[src] = 0
    for i in range(n):
        list[i][0] = dist[i]
    # Relax all edges | V | - 1 times. A simple shortest path from src to any other vertex can have at-most |V| - 1 edges
    for i in range(n-1):
        # Update dist value and parent index of the adjacent vertices of the picked vertex. Consider only those vertices which are still in queue.
        for u, v, w in graph:
            if dist[u] != float("inf") and dist[u]+w < dist[v]:
                dist[v] = dist[u]+w
        for j in range(n):
            list[j][i+1] = dist[j]
    # Step 3: check for negative-weight cycles. The above step guarantees shortest distances if graph doesnt contain negative weight cycle. If we get a shorter path, then there is a cycle.
    cycle = 0
    for u, v, w in graph:
        if dist[u] != float("Inf") and dist[u] + w < dist[v]:
            print("Graph has a negative weight cycle")
            cycle = 1
            break
    if cycle == 0:
        print('Distance from source vertex',src)
        '''
        print('Vertex \t Distance from source')
        for i in range(len(dist)):
            print(i,'\t',dist[i])
        '''
        for i in range(n):
            for j in range(n):
                print(list[i][j], end = ' ')
            print()

BellmanFord(0)