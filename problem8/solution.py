import collections

def bfs(graph, s, t, parent):
    """
    Returns true if there is a path from
    source 's' to sink 't' in residual graph.
    Also fills parent[] to store the path.
    """
    
    row = len(graph)

    # Mark all the vertices as not visited
    visited = [False] * row

    # Create a queue for BFS
    queue = collections.deque()

    # Mark the source node as visited and enqueue it
    queue.append(s)
    visited[s] = True

    # Standard BFS loop
    while queue:
        u = queue.popleft()

        # Get all adjacent vertices of the dequeued vertex u
        # If an adjacent has not been visited, then mark it
        # visited and enqueue it
        for ind, val in enumerate(graph[u]):
            if (visited[ind] == False) and (val > 0):
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    # If we reached sink in BFS starting from source, then return
    # true, else false
    return visited[t]

# Returns the maximum flow from s to t in the given graph
def edmonds_karp(graph, source, sink):
    row = len(graph)
    
    # This array is filled by BFS and to store path
    parent = [-1] * row

    max_flow = 0  # There is no flow initially

    # Augment the flow while there is path from source to sink
    while bfs(graph, source, sink, parent):
        # Find minimum residual capacity of the edges along the
        # path filled by BFS. Or we can say find the maximum flow
        # through the path found.
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        # Add path flow to overall flow
        max_flow += path_flow

        # update residual capacities of the edges and reverse edges
        # along the path
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow
    
def transform_graph(graph, sources, targets):
    new_graph_len = len(graph) + 2
    
    new_graph = [[0 for _ in range(new_graph_len)] for _ in range(new_graph_len)]
    
    for i in range(new_graph_len):
        for j in range(new_graph_len):
            if i == 0 and j in sources:
                new_graph[i][j + 1] = float("Inf")
                
            elif i in targets and j == new_graph_len - 1:
                new_graph[i + 1][j] = float("Inf")
                
            elif 1 <= i <= new_graph_len - 2 and 1 <= j <= new_graph_len - 2:
                new_graph[i][j] = graph[i - 1][j - 1]
    return new_graph
    
    
def solution(entrances, exits, path):
    new_graph = transform_graph(path, entrances, exits)
    return edmonds_karp(new_graph, 0, len(new_graph) - 1)
