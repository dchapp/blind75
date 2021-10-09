from collections import deque
import pprint


def to_graph(grid):
    adj_list = {}
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                adj_list[(i,j)] = []
                neighbors = [
                (i-1, j),
                (i+1, j),
                (i, j-1),
                (i, j+1)]
                for n_i, n_j in neighbors:
                    if n_i >= 0 and n_i < n and n_j >= 0 and n_j < n and grid[n_i][n_j] == 1:
                        adj_list[(i,j)].append((n_i, n_j))
    return adj_list


def add_shoreline(current_shoreline, current_node, n, graph):
    row, col = current_node
    neighbors = [
    (row-1, col),
    (row+1, col),
    (row, col-1),
    (row, col+1)
    ]
    for neighbor in neighbors:
        if neighbor not in graph:
            n_row, n_col = neighbor
            if n_row >= 0 and n_row < n and n_col >= 0 and n_col < n:
                current_shoreline.add(neighbor)
    return current_shoreline
                
        
def connected_components(graph, n):
    
    visited = set()
    
    def bfs(node, n, graph):
        component = set()
        queue = deque([node])
        row, col = node
        shoreline = set()
        while queue:
            current = queue.popleft()
            add_shoreline(shoreline, current, n, graph)
            visited.add(current)
            component.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return component, shoreline
    
    # Store mapping:
    # - From integer connected component IDs 
    # - To dict of connected component size, shoreline cell indices
    ccid_to_data = {}
    
    current_id = 0
    for node in graph:
        if node not in visited:
            component, shoreline = bfs(node, n, graph)
            ccid_to_data[current_id] = {"size": len(component), "shoreline": shoreline}
            current_id += 1
    return ccid_to_data



def invert_mapping(ccid_to_data):
    shoreline_cell_to_components = {}
    for ccid,data in ccid_to_data.items():
        shoreline_cells = data["shoreline"]
        for coords in shoreline_cells:
            if coords not in shoreline_cell_to_components:
                shoreline_cell_to_components[coords] = [ccid]
            else:
                shoreline_cell_to_components[coords].append(ccid)
    return shoreline_cell_to_components




class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        graph = to_graph(grid)
        
        if len(graph) == n**2:
            return n**2
        
        ccid_to_data = connected_components(graph, n)
        
        if len(ccid_to_data) == 0:
            return 1
        
        #pprint.pprint(ccid_to_data)
        
        coords_to_components = invert_mapping(ccid_to_data)
        #pprint.pprint(coords_to_components)
        
        largest_island = 0
        for k,v in coords_to_components.items():
            curr_island = 1
            for ccid in v:
                curr_island += ccid_to_data[ccid]["size"]
            if curr_island > largest_island:
                largest_island = curr_island
        
        return largest_island
        
        
        
