from graph import Graph

def shortestPath(adjacency, start, end):
    if start == end:
        return 0

    graph = Graph()

    for a in adjacency:
        graph.addEdge(a[0], a[1])

    queue = [(start, 0)]

    visited = set()

    while len(queue) > 0:
        
        vertex = queue[0][0]
        distance = queue[0][1] + 1

        neighbors = graph.getNeighbors(vertex)

        for n in neighbors:
            if n in visited:
                continue
            if n == end:
                return distance
            else:
                queue.append((n,distance))
                visited.add(n)

        
        
        queue.pop(0)
        

    return -1
        
        
