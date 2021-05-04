from collections import deque

class Node:
    def __init__(self, node_name):
        self.node_name = node_name
        self.visited = False
        self.adjacent_node = []

    def add_connection(self, other_node):
        self.adjacent_node.append(other_node)
        other_node.adjacent_node.append(self)

def create_graph(node1, node2, graph):

    if node1 not in graph:
        current_node1 = Node(node1)
        graph[node1] = current_node1
    else:
        current_node1 = graph[node1]

    if node2 not in graph:
        current_node2 = Node(node2)
        graph[node2] = current_node2
    else:
        current_node2 = graph[node2]

    current_node1.add_connection(current_node2)

    return graph

def BFS(graph, s_node):
    B_queue = deque()
    cnt = 0

    for node in graph.values():
        node.visited = False

    graph[s_node.node_name].visited = True
    B_queue.append(s_node)
    while B_queue:
        val = B_queue.popleft()
        # print("val : ", val.node_name, graph[val].adjacent_node)
        for i_node in graph[val.node_name].adjacent_node:
            if i_node.visited == False:
                i_node.visited = True
                cnt += 1
                B_queue.append(i_node)

    return cnt

N = int(input())
edge = int(input())

graph = {}
for i in range(edge):
    node1, node2  = input().split()
    graph = create_graph(node1, node2, graph)

n_node = Node('1')
print(BFS(graph, n_node))





