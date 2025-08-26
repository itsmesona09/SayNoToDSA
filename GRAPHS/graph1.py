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
    def print_path(self, start, end, path = []):
        # add the start node to the path
        path = path + [start]
        
        # CASE 1
        # check if the start and the end points are equal
        # if equal return the curr path appended with the start node
        if start == end:
            return path
        
        # CASE 2
        # if the start node is not in the graph, return None
        if start not in self.graph:
            return None
        
        # for each node in the adjacency list starting with the start node 
        for node in self.graph[start]:
            
            # if the node is not in the path
            # ensures that the recursive search doesn't revisit the nodes already incl
            if node not in path:
                # recursively call the print path function such that it appends the node to the path
                # by the line path = path + [start]
                new_path = self.print_path(node, end, path)
                
                # if the path is not empty, return the path
                if new_path:
                    return new_path
        return None

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
    end = "Toronto"
    print(f"The path from {start} to {end} is: ",graph.print_path(start, end))