class Graph:

    @staticmethod
    def node_hash(node):
        return node

    def __init__(self, nodes_count, hash_function):
        self.__node_count = nodes_count
        self.__edge_count = 0

        self.__hash_function = Graph.node_hash if hash_function is None else hash_function

        self.__adjacency_list = {
            self.__hash_function(i): [] for i in range(0, self.__node_count)
        }

    def add_edge(self, first, second):
        self.__adjacency_list[first].append(second)
        self.__adjacency_list[second].append(first)

        self.__edge_count += 1

    def remove_edge(self, first, second):
        if first in self.__adjacency_list[second]:
            self.__adjacency_list[first].remove(second)
            self.__adjacency_list[second].remove(first)

            self.__edge_count -= 1

    def is_adjacent(self, head, tail):
        neighbors = self.__adjacency_list.get(head, [])
        return tail in neighbors

    @property
    def edges(self):
        answer = set()
        for first in range(0, self.__node_count):
            for second in self.__adjacency_list[self.__hash_function(first)]:
                answer.add((self.__hash_function(first), second))

        return answer

    def BFS(self, source, destination):
        queue = [source]
        seen = {source: 0}

        while len(queue) != 0:
            top = queue.pop()
            # print(queue)
            # print(top)
            for edge in self.get_neighbors(top):
                if edge not in seen.keys():
                    seen[edge] = seen[top] + 1
                    # print(f'[log]: {seen[edge]}, {seen[top]}, {top}')
                    queue.insert(0, edge)
        # print(seen)
        return seen.get(destination, float('-inf'))

    def get_neighbors(self, node):
        return self.__adjacency_list[node]

    def show(self):
        print(self.__adjacency_list)

    def grid_complement(self, width, height):
        complement = initialize_grid_graph(width, height)

        for edge in self.edges:
            complement.remove_edge(*edge)

        return complement


def grid_hash(width, height):
    def hash_function(node):
        return node // height + 1, node % height + 1

    return hash_function


def initialize_grid_graph(width, height):
    graph = Graph(width * height, hash_function=grid_hash(width, height))

    for x in range(1, width + 1):
        for y in range(1, height + 1):
            if x + 1 <= width:
                graph.add_edge((x, y), (x + 1, y))
            if y + 1 <= height:
                graph.add_edge((x, y), (x, y + 1))

    return graph
