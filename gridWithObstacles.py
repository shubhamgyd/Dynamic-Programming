
def recursion(x, y, grid):
  if x >= 0 and y >= 0 and grid[x][y] == -1:
    return 0
  if x == 0 and y == 0:
    return 1
  if x < 0 or y < 0:
    return 0

  left = recursion(x, y-1, grid)

  top = recursion(x-1, y, grid)

  return left + top

def memoization(x, y, grid, dp):
  if x >= 0 and y >= 0 and grid[x][y] == -1:
    return 0
  if x == 0 and y == 0:
    return 1
  if x < 0 or y < 0:
    return 0   
  if dp[x][y] != -1:
    return dp[x][y]

  left = memoization(x, y-1, grid, dp)

  top = memoization(x-1, y, grid, dp)

  dp[x][y] = left + top
  return dp[x][y]

def tabulation(N, M, grid):
  dp = [[0 for i in range(M+1)] for j in range(N+1)]
  dp[1][1] = 1
  for x in range(1, N+1):
    for y in range(1, M+1):
      if x == 1 and y == 1:
        continue
      if x > 0 and y > 0 and grid[x-1][y-1] == -1:
        continue
      left = dp[x][y-1]
      top = dp[x-1][y]
      dp[x][y] = left + top
  return dp[N][M]

def spaceOptimization(N, M, grid):
  prev = [0 for i in range(M+1)]
  for x in range(1, N+1):
    curi = [0 for i in range(M+1)]
    for y in range(1, M+1):
      if x == 1 and y == 1:
        curi[y] = 1
        continue
      if x > 0 and y > 0 and grid[x-1][y-1] == -1:
        continue
      left = curi[y-1]
      top = prev[y]
      curi[y] = left + top
    prev = curi.copy()
  return prev[M]

def gridWithObstacles(N, M, grid):
  print("Recursion", recursion(N-1, M-1, grid))
  dp = [[-1 for i in range(M)] for j in range(N)]
  print("Memoization",memoization(N-1, M-1, grid, dp))
  print("Tabulation", tabulation(N, M, grid))
  print("SpaceOptimization", spaceOptimization(N, M, grid))

grid = [[0, 0, 0], [0, -1, 0], [0, 0, 0]]
N = len(grid)
M = len(grid[0])
gridWithObstacles(N, M, grid)