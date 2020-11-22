import math
maxsize = float('inf')

def copyToFinal(curr_path):
    final_path[:n + 1] = curr_path[:]
    final_path[n] = curr_path[0]


def firstMin(adj, i):
    min = maxsize
    for k in range(n):
        if adj[i][k] < min and i != k:
            min = adj[i][k]

    return min


def secondMin(adj, i):
    first, second = maxsize, maxsize
    for j in range(n):
        if i == j:
            continue
        if adj[i][j] <= first:
            second = first
            first = adj[i][j]

        elif (adj[i][j] <= second and
              adj[i][j] != first):
            second = adj[i][j]

    return second


def TSPRec(adj, curr_bound, curr_weight,
           level, curr_path, visited):
    global final_res

    # base case is when we have reached level N
    # which means we have covered all the nodes once
    if level == n:

        # check if there is an edge from
        # last vertex in path back to the first vertex
        if adj[curr_path[level - 1]][curr_path[0]] != 0:

            # curr_res has the total weight
            # of the solution we got
            curr_res = curr_weight + adj[curr_path[level - 1]][curr_path[0]]
            if curr_res < final_res:
                copyToFinal(curr_path)
                final_res = curr_res
        return

    # for any other level iterate for all vertices
    # to build the search space tree recursively
    for i in range(n):

        # Consider next vertex if it is not same
        # (diagonal entry in adjacency matrix and
        #  not visited already)
        if (adj[curr_path[level - 1]][i] != 0 and
                visited[i] == False):
            temp = curr_bound
            curr_weight += adj[curr_path[level - 1]][i]

            # different computation of curr_bound
            # for level 2 from the other levels
            if level == 1:
                curr_bound -= ((firstMin(adj, curr_path[level - 1]) +
                                firstMin(adj, i)) / 2)
            else:
                curr_bound -= ((secondMin(adj, curr_path[level - 1]) +
                                firstMin(adj, i)) / 2)

                # curr_bound + curr_weight is the actual lower bound
            # for the node that we have arrived on.
            # If current lower bound < final_res,
            # we need to explore the node further
            if curr_bound + curr_weight < final_res:
                curr_path[level] = i
                visited[i] = True

                # call TSPRec for the next level
                TSPRec(adj, curr_bound, curr_weight,
                       level + 1, curr_path, visited)

                # Else we have to prune the node by resetting
            # all changes to curr_weight and curr_bound
            curr_weight -= adj[curr_path[level - 1]][i]
            curr_bound = temp

            # Also reset the visited array
            visited = [False] * len(visited)
            for j in range(level):
                if curr_path[j] != -1:
                    visited[curr_path[j]] = True


def TSP(adj):
    # Calculate initial lower bound for the root node
    # using the formula 1/2 * (sum of first min +
    # second min) for all edges. Also initialize the
    # curr_path and visited array
    curr_bound = 0
    curr_path = [-1] * (n + 1)
    visited = [False] * n

    # Compute initial bound
    for i in range(n):
        curr_bound += (firstMin(adj, i) +
                       secondMin(adj, i))

        # Rounding off the lower bound to an integer
    curr_bound = math.ceil(curr_bound / 2)

    # We start at vertex 1 so the first vertex
    # in curr_path[] is 0
    visited[0] = True
    curr_path[0] = 0

    # Call to TSPRec for curr_weight
    # equal to 0 and level 1
    TSPRec(adj, curr_bound, 0, 1, curr_path, visited)


def tsp(graph, v, currPos, n, count, cost, mincost):
    if count == n and graph[currPos][0]:
        if mincost[0] > cost + graph[currPos][0]:
            mincost[0] = cost + graph[currPos][0]
        return

    # BACKTRACKING STEP
    # Loop to traverse the adjacency list
    # of currPos node and increasing the count
    # by 1 and cost by graph[currPos][i] value
    for i in range(n):
        if not v[i] and graph[currPos][i]:
            # Mark as visited
            v[i] = True
            tsp(graph, v, i, n, count + 1,
                cost + graph[currPos][i], mincost)

            # Mark ith node as unvisited
            v[i] = False


# Driver code

# n is the number of nodes i.e. V
if __name__ == '__main__':
    n = 4 #int(input("Enter size of the array: "))
    graph = [[0,10,15,20],[10,0,35,25],[15,35,0,30],[20, 25,30,0]]     # [[0 for i in range(n)] for j in range(n)]
    '''
    for i in range(n):
        for j in range(n):
            graph[i][j] = int(input())
    '''
    # Boolean array to check if a node
    # has been visited or not
    v = [False for i in range(n)]

    # Mark 0th node as visited
    v[0] = True
    mincost = [99999]
    # Find the minimum weight Hamiltonian Cycle
    tsp(graph, v, 0, n, 1, 0, mincost)   # backtracking
    print(mincost[0])

    final_path = [None] * (n + 1)

    # Stores the final minimum weight
    # of shortest tour.
    final_res = maxsize
    # Branch and Bound
    TSP(graph)

    print("Minimum cost :", final_res)
    print("Path Taken : ", end=' ')
    for i in range(n + 1):
        print(final_path[i], end=' ')


