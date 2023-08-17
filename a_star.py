class Node:
    """A node class for A* Pathfinding."""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic cost from current node to end node
        self.f = 0  # Total cost

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze."""

    #create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    #initialize both open and closed list
    open_list = []
    closed_list = []

    #add the start node
    open_list.append(start_node)

    #loop until the end is found
    while len(open_list) > 0:

        #get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        #remove current from open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        #found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        #gnerate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:  # Adjacent squares

            #get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            #ensure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
                    len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                continue

            #ensure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            #create new node
            new_node = Node(current_node, node_position)

            #append
            children.append(new_node)

        #loop through children
        for child in children:
            # Child is on the closed list
            if child in closed_list:
                continue

            #create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                    (child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            #child is already in the open list
            if child in open_list:
                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

            #add the child to the open list
            open_list.append(child)

    return None


maze = [
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

start = (0, 0)
end = (7, 6)

path = astar(maze, start, end)
print(path)
