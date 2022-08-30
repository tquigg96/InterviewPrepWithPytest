from collections import defaultdict as dd

class Graph:
    def __init__(self):

        self.graph = dd(list)

    def addEdge(self,a, b):
        self.graph[a].append(b)

    def BFS(self, start):

        visited = []

        queue = []

        queue.append(start)
        visited.append(start)

        while queue:
            start = queue.pop()
            