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
    
    # print the path from the start to the end node using depth first search
    def print_path(self, start, end, path=None):
        
        if path is None:
            path = []

        # add the start node to the path
        path = path + [start]

        # CASE 1
        # check if the start and the end points are equal
        # if equal return the curr path appended with the start node
        if start == end:
            return [path]

        # CASE 2
        # if the start node is not in the graph, return None
        if start not in self.graph:
            return []

        paths = []
        # iterating over the adjacency list of the `start` node in the graph.
        for node in self.graph[start]:

            # if the node is not in the path
            # ensures that the recursive search doesn't revisit the nodes already incl
            if node not in path:
                # recursively call the print path function such that it appends the node to the path
                # by the line path = path + [start]
                new_path = self.print_path(node, end, path)

                # for each path in the new path, append it to the `paths` list
                for p in new_path:
                    paths.append(p)

        return paths

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