from collections import defaultdict

def dfs(node, parent, graph, colors, count, res):
    # Count the colors in the subtree of node
    color_count = defaultdict(int)
    color_count[colors[node-1]] += 1
    
    for child in graph[node]:
        if child != parent:
            child_color_count = dfs(child, node, graph, colors, count, res)
            for color, cnt in child_color_count.items():
                color_count[color] += cnt
    
    # Find the dominating colors in the subtree of node
    dominating_colors = [color for color, cnt in color_count.items() if cnt == max(color_count.values())]
    res[node-1] = sum(dominating_colors)
    
    return color_count

def solve():
    n = int(input())
    colors = list(map(int, input().split()))
    graph = defaultdict(list)
    for _ in range(n-1):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    res = [0] * n
    dfs(1, -1, graph, colors, {}, res)
    print(' '.join(map(str, res)))

solve()

# RE
# https://codeforces.com/problemset/submission/600/261453593