from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        n_rows = len(image)
        n_cols = len(image[0])
        
        visited = set()
        
        queue = deque([(sr, sc)])
        
        while queue:
            
            row, col = queue.popleft()
            visited.add((row, col))
            curr_color = image[row][col]
            image[row][col] = newColor
            
            if row > 0:
                # Has upper neighbor
                if (row-1, col) not in visited and image[row-1][col] == curr_color:
                    queue.append((row-1, col))
            
            if row < n_rows-1:
                # Has lower neighbor
                if (row+1, col) not in visited and image[row+1][col] == curr_color:
                    queue.append((row+1, col))
            
            if col > 0:
                # Has left neighbor
                if (row, col-1) not in visited and image[row][col-1] == curr_color:
                    queue.append((row, col-1))
            
            if col < n_cols-1:
                # Has right neighbor
                if (row, col+1) not in visited and image[row][col+1] == curr_color:
                    queue.append((row, col+1))
                    
        return image
            
        
