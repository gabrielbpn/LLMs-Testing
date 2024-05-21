def dominating_colours(n, colours, edges):
    # Create an adjacency list representation of the tree
    graph = {i: [] for i in range(1, n+1)}
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # Function to find dominating colours in the subtree rooted at v
    def dfs(v):
        colour_counts = {i: 0 for i in range(1, n+1)}
        stack = [v]
        visited = set()
        
        while stack:
            u = stack.pop()
            if u not in visited:
                visited.add(u)
                for neighbor in graph[u]:
                    colour_counts[neighbor] += 1
                    stack.append(neighbor)

        dominating_colours_sum = sum(counts.count(i) for i, counts in colour_counts.items())
        return dominating_colours_sum

    # Calculate the sum of dominating colours for each vertex
    dominating_colours_sums = []
    visited = set()
    for v in range(1, n+1):
        if v not in visited:
            visited.add(v)
            dominating_colours_sums.append(dfs(v))

    return dominating_colours_sums


# Read the input and solve the problem
n = int(input())
colours = list(map(int, input().split()))
edges = []
for _ in range(n-1):
    edge = tuple(map(int, input().split()))
    edges.append(edge)

result = dominating_colours(n, colours, edges)
print(*result, sep=' ')

# RE
# https://codeforces.com/problemset/submission/600/261580483