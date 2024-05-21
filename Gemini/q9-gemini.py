from collections import Counter


def dfs(graph, node, color_counts, parent_color):
  """
  Performs a depth-first search on the tree.
  Updates the color counts for the current node and its children.

  Args:
      graph: Adjacency list representation of the tree.
      node: Current node being visited.
      color_counts: Dictionary keeping track of color counts for each node.
      parent_color: Color of the parent node (used to avoid double counting).
  """
  color_counts[node] += color_counts[parent_color]
  color_counts[node] -= 1  # Remove parent's contribution to this node's count

  # Update child nodes' color counts
  for child in graph[node]:
    dfs(graph, child, color_counts, color_counts[node])

    # Update dominant color sum for current node
    if color_counts[child] >= color_counts[node]:
      color_counts[node] = color_counts[child] + 1


def solve(n, colors, graph):
  """
  Solves the problem by performing DFS and calculating dominant color sums.

  Args:
      n: Number of vertices in the tree.
      colors: List containing the color of each vertex.
      graph: Adjacency list representation of the tree.

  Returns:
      List containing the sum of dominating colors for each vertex.
  """
  color_counts = Counter(colors)  # Count occurrences of each color
  dfs(graph, 1, color_counts, 0)  # Start DFS from root (node 1) with parent color 0

  # Remove the root's color from its own dominant color sum
  color_counts[1] -= 1

  return [color_counts[i] for i in range(1, n + 1)]


if __name__ == "__main__":
  n = int(input())
  colors = list(map(int, input().split()))
  graph = [[] for _ in range(n + 1)]  # Adjacency list (1-indexed)

  # Build the tree
  for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)

  result = solve(n, colors, graph)
  print(*result)

# WA
# https://codeforces.com/problemset/submission/600/261451326