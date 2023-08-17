import heapq  #for priority queue

def dijkstra(graph, start):
    #graph is represented as {node1: {node2: weight, node3: weight}, ...}

    #initialize the shortest path dictionary with infinities
    shortest_path = {vertex: float('infinity') for vertex in graph}
    shortest_path[start] = 0

    #(distance, vertex) pairs. The priority queue is initialized with the start vertex and distance 0.
    priority_queue = [(0, start)]

    while priority_queue:
        #get the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(priority_queue)

        #ensure not to process a vertex more than once
        if current_distance > shortest_path[current_vertex]:
            continue

        #consider all neighbors of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            #if a shorter path to the neighbor has been found, update the shortest path
            if distance < shortest_path[neighbor]:
                shortest_path[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_path

#example
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

print(dijkstra(graph, 'A'))
