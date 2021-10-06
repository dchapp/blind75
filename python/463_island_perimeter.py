

def get_initial(grid):
    n_rows = len(grid)
    n_cols = len(grid[0])
    row, col = None, None
    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == 1:
                return i, j
    return None


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        DFS thing to find connected component
        Whenever we visit, we'll add a number of sides equal to 4 - num_parents - num_outgoing
        num_parents will always be 1 so we can actually simplify to 3 - num_outgoing and handle the initial node as a special case
        """
        n_rows = len(grid)
        n_cols = len(grid[0])
        
        # Find initial land cell
        row, col = get_initial(grid) 
        total_perimeter = 0
        visited = set()
        stack = [(row, col)]
        
        while stack:
            row, col = stack.pop()
            if (row, col) in visited:
                continue
            visited.add((row, col))
            perimeter = 4

            if row > 0:
                neighbor = (row-1, col)
                if grid[row-1][col] == 1:
                    perimeter -= 1
                    if neighbor not in visited:
                        stack.append(neighbor)

            if row < n_rows-1:
                neighbor = (row+1, col)
                if grid[row+1][col] == 1:
                    perimeter -= 1
                    if neighbor not in visited:
                        stack.append(neighbor)

            if col > 0:
                neighbor = (row, col-1)
                if grid[row][col-1] == 1:
                    perimeter -= 1
                    if neighbor not in visited:
                        stack.append(neighbor)
                
            if col < n_cols-1:
                neighbor = (row, col+1)
                if grid[row][col+1] == 1:
                    perimeter -= 1
                    if neighbor not in visited:
                        stack.append(neighbor)
            
            #print(f"contribution from {row},{col} = {perimeter}")
            total_perimeter += perimeter
            
            
        return total_perimeter     
