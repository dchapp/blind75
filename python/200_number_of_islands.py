

def to_graph(grid):
    """
    Build adjacency list representation of graph
    Land cells in grid are connected if they are vertically or horizontally adjacent
    """
    adj_list = {}
    n_rows = len(grid)
    n_cols = len(grid[0])
    land_val = "1"
    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == land_val:
                adj_list[(i,j)] = []
                if i > 0 and grid[i-1][j] == land_val:
                    adj_list[(i,j)].append((i-1,j))
                if i < n_rows-1 and grid[i+1][j] == land_val:
                    adj_list[(i,j)].append((i+1,j))
                if j > 0 and grid[i][j-1] == land_val:
                    adj_list[(i,j)].append((i,j-1))
                if j < n_cols-1 and grid[i][j+1] == land_val:
                    adj_list[(i,j)].append((i,j+1))
    return adj_list
            


def num_connected_components(graph):
    """
    DFS-based CC count
    """
    seen = set()
    def dfs(node, component_size):
        if node not in seen:
            seen.add(node)
            component_size += 1
            for neighbor in graph[node]:
                if neighbor not in seen:
                    dfs(neighbor, component_size)
        return component_size
    
    num_connected_components = 0
    for node in graph:
        if dfs(node, 0) != 0:
            num_connected_components += 1
            
    return num_connected_components
        


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        graph_repr = to_graph(grid)
        return num_connected_components(graph_repr)
        
