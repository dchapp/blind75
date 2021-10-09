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
                
        
def connected_components(graph, n):
    
    visited = set()
    shoreline_to_ccid = {}
    
    def bfs(node, size, n, graph, ccid):
        queue = deque([node])
        while queue:
            # Track BFS visitation
            current = queue.popleft()
            if current not in visited:
                visited.add(current)
                # Update component size
                size += 1
                # Update shoreline mapping
                row, col = current
                shoreline_candidates = [
                (row-1, col),
                (row+1, col),
                (row, col-1),
                (row, col+1)]
                for n_row, n_col in shoreline_candidates:
                    if (n_row, n_col) not in graph and n_row >= 0 and n_row < n and n_col >= 0 and n_col < n:
                        if (n_row, n_col) not in shoreline_to_ccid:
                            shoreline_to_ccid[(n_row, n_col)] = {ccid}
                        else:
                            shoreline_to_ccid[(n_row, n_col)].add(ccid)
                # BFS visit
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return size
    
    ccid_to_size = {}
    
    ccid = 0
    for node in graph:
        if node not in visited:
            size = bfs(node, 0, n, graph, ccid)
            ccid_to_size[ccid] = size
            ccid += 1
    return ccid_to_size, shoreline_to_ccid


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        graph = to_graph(grid)
        
        if len(graph) == n**2:
            return n**2
        
        if len(graph) == 0:
            return 1
        
        ccid_to_size, shoreline_to_ccid = connected_components(graph, n)
        
        #pprint.pprint(ccid_to_size)
        #pprint.pprint(shoreline_to_ccid)
        
        largest_island = 0
        for ccid_list in shoreline_to_ccid.values():
            current_island = 1
            for ccid in ccid_list:
                current_island += ccid_to_size[ccid]
            if current_island > largest_island:
                largest_island = current_island
        
        return largest_island
        
