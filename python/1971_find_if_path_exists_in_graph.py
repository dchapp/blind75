import pprint

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        adj_list = {}
        for node,target in edges:
            if node not in adj_list:
                adj_list[node] = [target]
            else:
                adj_list[node].append(target)
            if target not in adj_list:
                adj_list[target] = [node]
            else:
                adj_list[target].append(node)
        seen = set()
        
        #pprint.pprint(adj_list) 
         
        def bfs(node: int, target: int) -> bool:
            #print(seen)
            if node == target:
                return True
            else:
                for neighbor in adj_list[node]:
                    #print(neighbor)
                    if neighbor not in seen:
                        seen.add(neighbor)
                        if bfs(neighbor, target):
                            return True
                return False
        
        
        return bfs(start, end)
