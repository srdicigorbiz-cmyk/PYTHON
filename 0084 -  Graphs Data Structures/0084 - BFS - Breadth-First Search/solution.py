from graph import Graph

def bfs(adjacency, start):
    graph = Graph()

    graph.addVertex(start)

    for adj in adjacency:
        graph.addEdge(adj[0], adj[1])
    
    queue = [start]

    visited = set()

    result = []

    while len(queue) > 0:
        
        edge = queue[0]

        neighbors = sorted(graph.getNeighbors(edge))
        
        visited.add(edge)
        
        result.append(edge)      
        
        for n in neighbors:
            if n not in visited:
                queue.append(n)
                visited.add(n)
        
        queue.pop(0)
    
    return result
        

    

    

