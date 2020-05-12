"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()     
        """
        Add a vertex to the graph.
        """

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        """
        Add a directed edge to the graph.
        """
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):

        q = Queue()
        q.enqueue(starting_vertex)

        visited = set()

        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        

    def dft(self, starting_vertex):

        s = Stack()
        s.push(starting_vertex)

        visited = set()

        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

        
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        pass  # TODO

    def dft_recursive(self, starting_vertex, visited=None):
        print(starting_vertex)

        if visited is None:
            visited = set()

        visited.add(starting_vertex)

        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                self.dft_recursive(child_vert, visited)

     
    def bfs(self, starting_vertex, destination_vertex,visited=None,  path=None):

        if visited is None:
            visited = set()
        
        if path is None:
            path = []

        q = Queue()
        q.enqueue(starting_vertex)
        
        if starting_vertex == destination_vertex:
            return path

        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                visited.add(v)
                path.append(v)
                if starting_vertex == destination_vertex:
                    return path
                for next_vert in self.get_neighbors(v):
                    print("bfs N", v)
                    if next_vert == destination_vertex:
                        path.append(next_vert)
                        return path
                    else:
                        q.enqueue(next_vert)
                   


        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO

    def dfs(self, starting_vertex, destination_vertex, path=None):

        if path is None:
            path = []

        s = Stack()
        s.push(starting_vertex)

        visited = set()

        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                path.append(v)
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    if next_vert == destination_vertex:
                        path.append(next_vert)
                        return path
                    s.push(next_vert)


        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):

        if visited is None:
            visited = set()
        
        if path is None:
            path = []

        visited.add(starting_vertex)

        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path

        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                new_path =self.dfs_recursive(child_vert, destination_vertex, visited, path)

                if new_path: 
                    return new_path
        return None

        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
     
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("bfs", graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("dfs", graph.dfs(1, 6))
    print("dfs_recursive", graph.dfs_recursive(1, 6))
