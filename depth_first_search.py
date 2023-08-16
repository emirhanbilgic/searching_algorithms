#graph is represented as an adjacency list: {node1: [neighbor1, neighbor2, ...], ...}
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

def dfs(graph, node, visited=None):
    #use a default mutable argument only if it's safe (in this case, we know it won't be modified)
    if visited is None:
        visited = set()
    
    #mark the current node as visited
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
    return visited

#start DFS from node A
dfs(graph, 'A')
