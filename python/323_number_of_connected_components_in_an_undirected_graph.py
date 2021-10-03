


def to_graph(n, edges):
    adj_list = {node:[] for node in range(n)}
    for src,dst in edges:
        adj_list[src].append(dst)
        adj_list[dst].append(src)
    return adj_list


def count_connected_components(graph):
    
    def dfs(node, visited):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited)
    
    visited = set()
    num_connected_components = 0
    for node in graph:
        if node not in visited:
            dfs(node, visited)
            num_connected_components += 1
    return num_connected_components


def dfs_solution(n, edges):
    graph = to_graph(n, edges)
    return count_connected_components(graph)



class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        return dfs_solution(n, edges)
        
        
