from graph import Graph

def isBipartite(adjacency, vertices):
    
    graph = Graph()

    for v in vertices:
        graph.addVertex(v)
    
    for a in adjacency:
        graph.addEdge(a[0], a[1])


    queue = list(graph.vertices.keys())
    
    colours = {0:[], 1:[]}

    for v in queue:
        if v not in colours[0]:
            if v not in colours[1]:
                colours[0].append(v)
        
        neighbors = graph.getNeighbors(v)
        
        if v in colours[0]:
            for n in neighbors:
                if n in colours[0]:
                    return False
                if n not in colours[1]:
                    colours[1].append(n)
        else:
            for n in neighbors:
                if n in colours[1]:
                    return False
                if n not in colours[0]:
                    colours[0].append(n)

    return True
