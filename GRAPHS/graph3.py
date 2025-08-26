class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edges(self, edges):
        for start, end in edges:
            if start in self.graph:
                self.graph[start].append(end)
            else:
                self.graph[start] = [end]
        return self.graph
    
    def print_path(self, start, end, path=None):
        # sourcery skip: for-append-to-extend, simplify-generator
        
        if path is None:
            path = []

        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph:
            return []

        paths = []
        for node in self.graph[start]:
            if node not in path:
                new_path = self.print_path(node, end, path)
                for p in new_path:
                    paths.append(p)

        return paths
    
    # print shortest path
    def shortest_path(self, start, end, path=None):
        # initialize shortest path
        shortest_path = None
        
        # append the node to the path that needs to be listed
        if path is None:
            path = []
        path = path + [start]
        
        # if start and end are equal, return the path
        if start == end:
            return path
        
        # if the given start is not in graph, return None
        if start not in self.graph:
            return None
        
        # for each node in the adjacency list from the start
        for node in self.graph[start]:
            # check if the node is not in the path to avoid recurrence during recursive calls
            if node not in path:
                # get the path from the graph
                new_path = self.shortest_path(node, end, path)
                # for the particular path, check if the shortest path is None
                # if None, simply assign the shortest path as the new path
                
                # if not, check if the len of the curr new path < len of the shortest path
                if new_path and (shortest_path is None or len(new_path) < len(shortest_path)):
                    # assign the new shortest path
                    shortest_path = new_path
        return shortest_path

if __name__ == "__main__":
    
    # given a list of tuples representing start and end points
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    
    graph = Graph()
    print(graph.add_edges(routes))
    
    print()
    
    start = "Mumbai"
    end = "New York"
    
    print(f"The path from {start} to {end} is: ",graph.print_path(start, end))
    
    print()
    
    print(f"The shortest path from {start} to {end} is :", graph.shortest_path(start, end))