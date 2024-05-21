
from collections import defaultdict

# Function to calculate the sum of dominating colors for each vertex
def sum_of_dominating_colors(n, colors, edges):
    # Create a default dictionary to store the counts of each color in the subtree of each vertex
    counts = defaultdict(lambda: defaultdict(int))
    # Create a dictionary to store the total sum of dominating colors for each vertex
    sums = {}

    # DFS function to traverse the tree and calculate the color counts
    def dfs(vertex, parent):
        # Initialize the color counts for the current vertex
        counts[vertex][colors[vertex-1]] = 1
        # Traverse all the neighbors of the current vertex
        for neighbor in edges[vertex]:
            # Skip the parent node
            if neighbor == parent:
                continue
            # Recursive call to DFS
            dfs(neighbor, vertex)
            # Update the color counts by adding the counts of the neighbor
            for color, count in counts[neighbor].items():
                counts[vertex][color] += count

    # Populate the edges list using the input
    edges = defaultdict(list)
    for x, y in edges_list1:
        edges[x].append(y)
        edges[y].append(x)

    # Call the DFS function with the root vertex 1
    dfs(1, 0)

    # Traverse all the vertices to compute the sum of dominating colors
    for vertex in range(1, n+1):
        # Initialize the sum for the current vertex
        sums[vertex] = 0
        # Find the color that dominates the subtree of the current vertex
        max_count = max(counts[vertex].values())
        # Add the dominating colors to the sum
        for color, count in counts[vertex].items():
            if count == max_count:
                sums[vertex] += color

    # Return the sums of dominating colors for each vertex
    return [sums[vertex] for vertex in range(1, n+1)]

# Example inputs
n1 = 4
colors1 = [1, 2, 3, 4]
edges_list1 = [(1, 2), (2, 3), (2, 4)]

n2 = 15
colors2 = [1, 2, 3, 1, 2, 3, 3, 1, 1, 3, 2, 2, 1, 2, 3]
edges_list2 = [(1, 2), (1, 3), (1, 4), (1, 14), (1, 15), (2, 5), (2, 6), (2, 7), (3, 8), (3, 9), (3, 10), (4, 11), (4, 12), (4, 13)]

# Call the function for the example inputs
print(sum_of_dominating_colors(n1, colors1, edges_list1))  # Output: [10, 9, 3, 4]
print(sum_of_dominating_colors(n2, colors2, edges_list2))  # Output: [6, 5, 4, 3, 2, 3, 3, 1, 1, 3, 2, 2, 1, 2, 3]

# RE
# https://codeforces.com/problemset/submission/600/261452711