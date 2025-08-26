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