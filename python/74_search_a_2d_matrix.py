
def binary_search(array, start_idx, end_idx, target):
    # assumes array is sorted in increasing order
    
    # Handle case where target not in array
    if start_idx == end_idx:
        if array[start_idx] == target:
            return start_idx
        else:
            return -1, (start_idx, end_idx)
    elif start_idx == end_idx-1:
        if array[start_idx] == target:
            return start_idx
        elif array[end_idx] == target:
            #print(f"array: {array}, array[end_idx] = {array[end_idx]}, target = {target}")
            return end_idx
        else:
            if target < array[end_idx]:
                return -1, start_idx
            else:
                return -1, end_idx
    else:
        midpoint_idx = start_idx + ((end_idx - start_idx) // 2)
        #print(f"start index = {start_idx}, end_idx = {end_idx}, midpoint index: {midpoint_idx}")
        midpoint_element = array[midpoint_idx]
        if midpoint_element == target:
            #print(f"midpoint element = {midpoint_element}, target = {target}")
            return midpoint_idx
        elif midpoint_element < target:
            # Recurse on upper half
            return binary_search(array, midpoint_idx, end_idx, target)
        else:
            # Recurse on lower half
            return binary_search(array, start_idx, midpoint_idx, target)
    

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Should be able to do this in O(log(N)) since we can binary search twice to get the answer
        - Once on first column (i.e., first element of each row) to figure out what row the target would be in
        - Once on that row to find the target or show that it doesn't exist
        """
        
        #test_array_even = list(range(10))
        #test_array_odd = list(range(11))
        #target = 7
        #test_array_even_missing = [1,2,3,5,6,7]        
        #test_array_odd_missing = [1,2,3,5,6,7,8]
        #missing_target = 4
        #print(binary_search([10, 11, 16, 20], 0, 3, 13))
        #assert test_array_even[binary_search(test_array_even, 0, len(test_array_even)-1, target)] == target
        #assert test_array_odd[binary_search(test_array_odd, 0, len(test_array_odd)-1, target)] == target
        ##print(binary_search(test_array_even_missing, 0, len(test_array_even_missing)-1, missing_target))
        #assert binary_search(test_array_even_missing, 0, len(test_array_even_missing)-1, missing_target) == -1
        #assert binary_search(test_array_odd_missing, 0, len(test_array_odd_missing)-1, missing_target) == -1
        
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        
        if n_rows == 1:
            row_search = binary_search(matrix[0], 0, n_cols-1, target)
            return isinstance(row_search, int)
        
        if n_cols == 1:
            col_search = binary_search([matrix[i][0] for i in range(n_rows)], 0, n_rows-1, target)

        first_column = [matrix[i][0] for i in range(n_rows)]
        row_search_result = binary_search(first_column, 0, n_rows-1, target)
        if isinstance(row_search_result, int):
            return True
        else:
            _, row = row_search_result
            #print(f"We know the target {target} must be in row {row}: {matrix[row][:]}")
            candidate_row = matrix[row]
            col_search_result = binary_search(candidate_row, 0, n_cols-1, target)
            return isinstance(col_search_result, int)
