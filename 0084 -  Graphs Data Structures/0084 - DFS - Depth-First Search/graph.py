class Graph:

    def __init__(self):
        self.vertices = {}

    def addVertex(self, key):
        if key not in self.vertices:
            self.vertices[key] = []

    def addEdge(self, u, v):
        self.addVertex(u)
        self.addVertex(v)
        if v not in self.vertices[u]:
            self.vertices[u].append(v)
        if u == v:
            return
        if u not in self.vertices[v]:
            self.vertices[v].append(u)

    def hasEdge(self, u, v):
        if u not in self.vertices:
            return False
        return v in self.vertices[u]

    def getNeighbors(self, key):
        if key not in self.vertices:
            return []
        return list(self.vertices[key])

    def removeEdge(self, u, v):
        if u in self.vertices and v in self.vertices[u]:
            self.vertices[u].remove(v)
        if u == v:
            return
        if v in self.vertices and u in self.vertices[v]:
            self.vertices[v].remove(u)

    def size(self):
        return len(self.vertices)
