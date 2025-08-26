class Graph:
    def __init__(self):
        # initializes an empty dictionary graph
        # start of a class representing a graph data structure
        # prepare the instance to store a graph related data (adjacency lists or nodes)
        self.graph = {}
    
    def add_edges(self, edges):
        # adds edges to the graph
        
        # iterate through the list of edges
        for start, end in edges:
            # for each starting point in the edge, add the end point to the adjacency list
            if start in self.graph:
                self.graph[start].append(end)
            # if the starting point is not in the graph, create a new 
            else:
                self.graph[start] = [end]
        # return the adjacency list
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
    
    # why output is ?
    # The path from Mumbai to New York is:  ['Mumbai', 'Paris', 'Dubai', 'New York', 'Mumbai', 'Paris', 'New York', 'Mumbai', 'Dubai', 'New York']

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