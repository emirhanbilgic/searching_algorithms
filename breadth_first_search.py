# source is: https://www.youtube.com/watch?v=tswq532WVF4&ab_channel=ThinkXAcademy

import collections #to use queue data structure

graph = {0 : [1,2,3] , 1: [0,2], 2: [0, 1, 4], 3: [0], 4: [2]}

def bfs(graph, root):
    visited = set() #creates a set
    queue = collections.deque([root])
    
    while queue:
        vertex = queue.popleft()
        visited.add(vertex)
        for i in graph[vertex]:
            if i not in visited:
                queue.append(i)
    print(visited)

bfs(graph, 0)
            
