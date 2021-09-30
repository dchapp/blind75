import itertools

class graph:
    def __init__(self, nodes=set(), edges=set()):
        self.nodes = nodes
        self.edges = edges
        self.adjacency_list = {}
        for node in nodes:
            self.adjacency_list[node] = []
        for edge in edges:
            src, dst = edge
            self.adjacency_list[src].append(dst)
            self.adjacency_list[dst].append(src)
    
    def dfs(self, node, tmp, visited):
        visited.add(node)
        for neighbor in self.adjacency_list[node]:
            if neighbor not in visited:
                tmp = self.dfs(neighbor, tmp, visited)
        return tmp
        
    def connected_components(self):
        visited = set()
        connected_components = []
        for node in self.nodes:
            if node not in visited:
                tmp = []
                connected_components.append(self.dfs(node, tmp, visited))
        return connected_components

def make_graph(stones: List[List[int]]) -> graph:
    row_to_stones = {}
    col_to_stones = {}
    for stone_idx, stone in enumerate(stones):
        row, col = stone
        if row not in row_to_stones:
            row_to_stones[row] = [stone_idx]
        else:
            row_to_stones[row].append(stone_idx)
        if col not in col_to_stones:
            col_to_stones[col] = [stone_idx]
        else:
            col_to_stones[col].append(stone_idx)
    nodes = set(range(len(stones)))
    edges = set()
    for row, stone_indices in row_to_stones.items():
        curr_edges = set([tuple(sorted(pair)) for pair in filter(lambda x: x[0] != x[1], itertools.product(stone_indices, stone_indices))])
        for edge in curr_edges:
            edges.add(edge)
    for col, stone_indices in col_to_stones.items():
        curr_edges = set([tuple(sorted(pair)) for pair in filter(lambda x: x[0] != x[1], itertools.product(stone_indices, stone_indices))])
        for edge in curr_edges:
            edges.add(edge)
    return graph(nodes, edges)
       
    
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph_repr = make_graph(stones)
        return len(stones) - len(graph_repr.connected_components())
        
