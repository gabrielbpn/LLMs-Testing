def is_mastapeece(mosaic):
    n = len(mosaic)
    mastapeece = [[None]*n for _ in range(n)]
    
    # Initialize the given mosaic
    for i in range(n):
        for j in range(n):
            if mosaic[i][j] == 'S':
                mastapeece[i][j] = 0
            elif mosaic[i][j] == 'G':
                mastapeece[i][j] = 1
    
    # Fill the rest of the tiles
    for i in range(n):
        for j in range(n):
            if mastapeece[i][j] is None:
                count_S = sum(mastapeece[x][y] for x in range(max(0, i-1), min(n, i+2)) 
                              for y in range(max(0, j-1), min(n, j+2)) if (x, y) != (i, j))
                count_G = sum(mastapeece[x][y] for x in range(max(0, i-1), min(n, i+2)) 
                              for y in range(max(0, j-1), min(n, j+2)) if (x, y) != (i, j))
                
                mastapeece[i][j] = 0 if count_S == 2 else 1
    
    # Check the condition
    for i in range(n):
        for j in range(n):
            if mastapeece[i][j] is None:
                return False
            count_S = sum(mastapeece[x][y] for x in range(max(0, i-1), min(n, i+2)) 
                          for y in range(max(0, j-1), min(n, j+2)) if (x, y) != (i, j))
            count_G = sum(mastapeece[x][y] for x in range(max(0, i-1), min(n, i+2)) 
                          for y in range(max(0, j-1), min(n, j+2)) if (x, y) != (i, j))
            
            if mastapeece[i][j] == 0 and count_S > 2 or count_G > 2:
                return False
    
    return True


def solve(mosaic):
    n = len(mosaic)
    
    if not is_mastapeece(mosaic):
        return "NONE"
    elif is_mastapeece(mosaic):
        return "UNIQUE"


# Request the input
n = int(input())
mosaic = [list(input()) for _ in range(n)]

# Solve and print the output
print(solve(mosaic))
if solve(mosaic) == "UNIQUE":
    for row in mosaic:
        print(''.join(row))

# RE
# https://codeforces.com/problemset/submission/1586/261580489