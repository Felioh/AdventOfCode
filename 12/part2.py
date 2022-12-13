import numpy as np
import pandas as pd
import parse
import sys

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def get_outgoing_edges(data, pos):
    res = []
    for d in DIRS:
        neighbor = [a+b for a, b in zip(pos, d)]
        if neighbor[0] < 0 or neighbor[1] < 0 or neighbor[0] >= len(data) or neighbor[1] >= len(data[0]):
            continue
        if ord(data[neighbor[0]][neighbor[1]]) >= ord(data[pos[0]][pos[1]]) - 1:
            res.append(tuple(neighbor))

    return res
        
def dijkstra_algorithm(data, start_node):
    unvisited_nodes = set([(x, y) for x in range(len(data)) for y in range(len(data[1]))])
    # unvisited_nodes.remove(start_node)
    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
    shortest_path = {}
 
    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}
 
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[start_node] = 0
    
    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = get_outgoing_edges(data, current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + 1 #graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
 
        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

def main():
    data = np.genfromtxt("/mnt/c/Users/felix/workspace/adventOfCode/12/in.txt", delimiter=1, dtype=str)
    start_pos = list(zip(*np.where(data == "a")))
    end_pos = list(zip(*np.where(data == "E")))[0]
    data[end_pos] = "z"
    paths = dijkstra_algorithm(data, end_pos)[1]
    shortest_path = min([paths[start] for start in start_pos])
    
    print(shortest_path)

if __name__ == '__main__':
    main()