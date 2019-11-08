from Graph import Graph
graph = Graph()
graph.read('first.txt')
print(graph.adj(1, 3))
print(graph.adj_edg(1))
print(graph.weight(1))
print(graph.weight(3))
print(graph.weight_edg(1, 3))
graph.enum()
