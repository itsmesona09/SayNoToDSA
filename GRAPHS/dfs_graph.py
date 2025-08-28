class Dfs:
    def __init__(self):
        self.graph = {}
        
    def adj_list(self, edges):
        for start, end in edges:
            if start in self.graph:
                self.graph[start].append(end)
            else:
                self.graph[start] = [end]
            
            if end not in self.graph:
                self.graph[end] = []

        return self.graph
    
    def dfs(self, graph, start, visited=None):
        # graph => adjacency list created from routes
        
        # instead of creating a set or a list for each call of the function
        # write a condition such that if the visited is only None, create a list or set
        if visited is None:
            # visited = set() if using sets
            visited = []

        # if using set use add
        visited.append(start)
        # print(start, end=' ')

        # for each adjacent nodes of the current node
        for node in graph[start]:
            # check if its already visited or not
            # if not, call the dfs function
            if node not in visited:
                self.dfs(graph, node, visited)
                
        return visited

if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    
    route = Dfs()
    graph = route.adj_list(routes)
    print(graph)
    
    print()
    
    start = "Mumbai"
    print(route.dfs(graph, start))