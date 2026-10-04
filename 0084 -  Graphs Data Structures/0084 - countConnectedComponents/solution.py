from graph import Graph

def countConnectedComponents(adjacency, vertices):
    
    graph = Graph()

    for v in vertices:
        graph.addVertex(v)
    
    for a in adjacency:
        graph.addEdge(a[0],a[1])

    def helper(s):
    
        queue = [s]

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

    queue = list(graph.vertices.keys())
    
    visited = set()

    counter = 0

    while len(queue) > 0:
        
        vertex = queue[0]

        if vertex not in visited:
            
            counter += 1
            bfs = helper(vertex)

            for b in bfs:
                visited.add(b)
            queue.pop(0)
        else:
            queue.pop(0)
            

    return counter