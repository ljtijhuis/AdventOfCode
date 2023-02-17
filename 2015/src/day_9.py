import itertools
import string
from typing import List
from src.file_utils import read_file

def addEdge(edges, v1, v2, distance):
    if v1 in edges:
        edges[v1][v2] = distance
    else:
        edges[v1] = dict()
        edges[v1][v2] = distance

def addVertice(vertices, v):
    if v not in vertices:
        vertices.append(v)

def calcLength(route: List[str], edges: dict):
    cost = 0
    for i in range(1, len(route)):
        cost += edges[route[i-1]][route[i]]
    return cost

def shortest_route(input: List[str]) -> int:
    # Build graph
    edges = dict()
    vertices = []
    for s in input:
        route, distance = s.split(' = ')
        v1, v2 = route.split(' to ')
        addEdge(edges, v1, v2, int(distance))
        addEdge(edges, v2, v1, int(distance))
        addVertice(vertices, v1)
        addVertice(vertices, v2)

    # iterate all routes and find min distance
    shortest = 10 ** 9
    for perm in itertools.permutations(vertices[1:], len(vertices) - 1):
        route = list(perm)
        route.insert(0, vertices[0])
        shortest = min(shortest, calcLength(route, edges))

    return shortest

def longest_route(input: List[str]) -> int:
    # Build graph
    edges = dict()
    vertices = []
    for s in input:
        route, distance = s.split(' = ')
        v1, v2 = route.split(' to ')
        addEdge(edges, v1, v2, int(distance))
        addEdge(edges, v2, v1, int(distance))
        addVertice(vertices, v1)
        addVertice(vertices, v2)

    # iterate all routes and find min distance
    longest = 0
    for perm in itertools.permutations(vertices, len(vertices)):
        route = list(perm)
        longest = max(longest, calcLength(route, edges))

    return longest

        



if __name__ == "__main__":
    input = read_file('/../input/day_9.txt')
    lines = input.splitlines()
    
    print(shortest_route(lines))
    print(longest_route(lines))