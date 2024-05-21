def solve(grid):
  """
  This function determines if there is a unique way to complete the mosaic 
  into a mastapeece, and if so, returns the completed grid.

  Args:
      grid: A list of strings representing the rows of the mosaic grid.

  Returns:
      A string representing "UNIQUE" if there is a unique solution, 
      "NONE" if there is no solution, or "MULTIPLE" if there are multiple 
      solutions. If the solution is unique, the function also returns 
      a list of strings representing the completed grid.
  """  
  n = len(grid)
  visited = [[False for _ in range(n)] for _ in range(n)]
  
  def dfs(row, col, color):
    """
    Performs a depth-first search to explore possible completions of the mosaic.

    Args:
        row: The current row index.
        col: The current column index.
        color: The color of the current tile ('S' or 'G').

    Returns:
        A string representing "UNIQUE" if a unique solution is found, 
        "INVALID" if the current configuration is invalid, or None 
        if no solution is found yet.
    """
    if not (0 <= row < n and 0 <= col < n):
      return None
    if visited[row][col]:
      return "INVALID"
    visited[row][col] = True
    
    # Check if the current cell is empty
    if grid[row][col] == '.':
      grid[row][col] = color
      
      # Check if all cells are filled
      if all(cell != '.' for row in grid for cell in row):
        return "UNIQUE"
      
      # Explore possibilities for the next cell
      for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        next_row, next_col = row + dx, col + dy
        result = dfs(next_row, next_col, 'G' if color == 'S' else 'S')
        if result == "UNIQUE":
          return result
        elif result == "INVALID":
          return result
      
      # Backtrack if no solution is found in this branch
      grid[row][col] = '.'
    
    # Check if the current tile has the expected number of adjacent tiles of the same color
    adj_count = 0
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
      next_row, next_col = row + dx, col + dy
      if 0 <= next_row < n and 0 <= next_col < n and grid[next_row][next_col] == color:
        adj_count += 1
    if adj_count != 2:
      return "INVALID"
    
    visited[row][col] = False
    return None

  # Start DFS from any empty cell
  for row in range(n):
    for col in range(n):
      if grid[row][col] == '.':
        result = dfs(row, col, 'S')
        if result == "UNIQUE":
          return "UNIQUE", grid
        elif result == "INVALID":
          return "NONE"
  
  # No solution found
  return "NONE"

if __name__ == "__main__":
  n = int(input())
  grid = [input() for _ in range(n)]
  result, completed_grid = solve(grid.copy())
  print(result)
  if result == "UNIQUE":
    for row in completed_grid:
      print(row)

# RE
# https://codeforces.com/problemset/submission/1586/261451336
