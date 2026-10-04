from graph import Graph

def isBipartite(adjacency, vertices):
    graph = Graph()
    for v in vertices:
        graph.addVertex(v)
    for a in adjacency:
        graph.addEdge(a[0], a[1])
    
    mark = {}

    for start_vertex in vertices:
        # Ha ezt a csúcsot már megfestettük egy korábbi körben, átlépjük
        if start_vertex in mark:
            continue
            
        # Új sziget/komponens indítása: az első kap egy színt (pl. 0)
        mark[start_vertex] = 0
        queue = [start_vertex]

        # BFS hullám indítása
        while len(queue) > 0:
            current = queue.pop(0)
            
            # Végigmegyünk a közvetlen szomszédokon
            for neighbor in graph.getNeighbors(current):
                if neighbor not in mark:
                    # Ha még nincs színe, kapja az ellenkezőjét
                    mark[neighbor] = 1 - mark[current]
                    queue.append(neighbor)
                elif mark[neighbor] == mark[current]:
                    # Ha már van színe, de azonos a miénkkel -> HIBA!
                    return False

    return True