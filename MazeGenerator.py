from random import randint

from Graph import initialize_grid_graph, grid_hash


def merge_sets(set_list, first, second):
    first_index, second_index = -1, -1

    for index, s in enumerate(set_list):
        if first in s:
            first_index = index
        if second in s:
            second_index = index

    if first_index != second_index:
        s1 = set_list[first_index]
        s2 = set_list[second_index]

        set_list.remove(s1)
        set_list.remove(s2)

        set_list.append(s1.union(s2))

        return True

    return False


def generate_maze(width, height):
    hash_function = grid_hash(width, height)
    count = width * height
    sets = [{(hash_function(i))} for i in range(0, count)]

    graph = initialize_grid_graph(width, height)

    condition = True
    while condition:
        edges = list(graph.edges)
        edge_index = randint(0, len(edges) - 1)
        edge = edges[edge_index]

        first, second = edge

        if merge_sets(sets, first, second):
            graph.remove_edge(first, second)

        condition = len(sets) != 1

    return graph
