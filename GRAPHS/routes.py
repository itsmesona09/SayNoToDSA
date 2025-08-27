class Graph:
    def __init__(self):
        self.graph = {}
        
    def adj_list(self, edges):
        for start, end in edges:
            if start in self.graph:
                self.graph[start].append(end)
            else:
                self.graph[start] = [end]
        return self.graph
    
    def print_path(self, start, end, path=None):
        if not path:
            path = []
            
        path = path + [start]
        
        if start == end:
            return [path]
        if start not in path:
            return []
        
        res = []
        for node in self.graph[start]:
            if node not in path:
                new_path = self.print_path(node, end, path)
                for p in new_path:
                    res.append(p)
        return res
    
    
    def shortest_path(self, start, end, path=None):
        shortest_path = None
        if path is None:
            path = []
        path = path + [start]
        
        if start == end:
            return [path]
        
        if start not in self.graph:
            return None
        
        for node in self.graph[start]:
            if node not in path:
                new_path = self.print_path(node, end, path)
                if new_path and (shortest_path is None or len(shortest_path) > len(new_path)):
                    shortest_path = new_path
        return shortest_path
    
if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    
    route = Graph()
    print(route.adj_list(routes))
    
    start = "Mumbai"
    end = "New York"
    print(route.print_path(start, end))
    
    print(route.shortest_path(start, end))