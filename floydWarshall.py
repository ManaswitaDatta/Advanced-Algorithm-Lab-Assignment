INF = 999


def floyd_warshall(vertex, adjacency_matrix):
    for k in range(0, vertex):
        for i in range(0, vertex):
            for j in range(0, vertex):
                # relax the distance from i to j by allowing vertex k as intermediate vertex
                # consider which one is better, going through vertex k or the previous value
                adjacency_matrix[i][j] = min(adjacency_matrix[i][j], adjacency_matrix[i][k] + adjacency_matrix[k][j])
    # pretty print the graph
    # o/d means the leftmost row is the origin vertex
    # and the topmost column as destination vertex
    print("o/d", end='')
    for i in range(0, vertex):
        print("\t{:d}".format(i + 1), end='')
    print()
    for i in range(0, vertex):
        print("{:d}".format(i + 1), end='')
        for j in range(0, vertex):
            if adjacency_matrix[i][j] > 900:
                print("\t{:d}".format(999), end='')
            else:
                print("\t{:d}".format(adjacency_matrix[i][j]), end='')
        print()

print("Enter number of vertices in the graph:- ")
n = int(input())
adjacency_matrix = [[0 for i in range(n)] for j in range(n)]
print("Enter the matrix")
for i in range(n):
    for j in range(n):
        adjacency_matrix[i][j] = int(input())
floyd_warshall(n, adjacency_matrix)
