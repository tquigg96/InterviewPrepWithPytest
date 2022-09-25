from collections import defaultdict as dd

class Graph:
    def __init__(self):

        self.graph = dd(list)

    def addEdge(self,a, b):
        self.graph[a].append(b)

    def DFS(graph, start, stack):

        stack.append(start)
        
        while (len(stack) > 0):
            current = stack.pop()
            print(current)

            for neighbor in graph[current]:
                stack.push(neighbor)

    def BFS(self, start, visited):

        if start in visited:
            return True

        visited.append(start)

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                visited.append(start)
