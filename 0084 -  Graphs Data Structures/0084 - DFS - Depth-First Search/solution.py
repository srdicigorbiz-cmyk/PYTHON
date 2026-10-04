from graph import Graph

def dfs(adjacency, start):
    
    graph = Graph()
    
    graph.addVertex(start)

    for a in adjacency:
        graph.addEdge(a[0], a[1])
        
    
    stack = [start]

    visited = set()

    result = []

    while len(stack)>0:
        
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)

            neighbors = sorted(graph.getNeighbors(vertex), reverse = True)
        
            for n in neighbors:
                if n not in visited:
                    stack.append(n)
        else:
            continue

    
    return result