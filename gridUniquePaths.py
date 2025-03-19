
def recursive(x, y, d):
  if x == 0 and y == 0:
    return 1
  if x < 0 or y < 0:
    return 0
  
  res = 0
  for dx, dy in d:
    res += recursive(x+dx, y+dy, d)
  
  return res

def memoization(x, y, d, dp):
  if x == 0 and y == 0:
    return 1
  if x < 0 or y < 0:
    return 0
  
  if dp[x][y] != -1:
    return dp[x][y]
  
  res = 0
  for dx, dy in d:
    res += memoization(x+dx, y+dy, d, dp)
  
  dp[x][y] = res
  return dp[x][y]

def tabulation(n, m):
  dp = [[0 for i in range(m+1)] for j in range(n+1)]
  dp[1][1] = 1
  d = [(-1, 0), (0, -1)]
  for x in range(1, n+1):
    for y in range(1, m+1):
      if x == 1 and y == 1:
        continue
      res = 0
      for dx, dy in d:
        res += dp[x+dx][y+dy]
      dp[x][y] = res
  return dp[n][m]

def spaceOptimization(n, m):
  prev = [0 for i in range(m+1)]
  d = [(-1, 0), (0, -1)]
  curi = [0 for i in range(m+1)]
  for x in range(1, n+1):
    for y in range(1, m+1):
      if x == 1 and y == 1:
        curi[y] = 1
        continue
      res = 0
      for dx, dy in d:
        if dx == -1:
          res += prev[y+dy]
        elif dx == 0:
          res += curi[y+dy]
      curi[y] = res
    prev = curi.copy()
  return prev[m]


def gridUniquePathExist(n, m):

  d = [(-1, 0), (0, -1)]
  # print(recursive(n-1, m-1, d))

  dp = [[-1 for i in range(m)] for j in range(n)]
  print("Memoization:",memoization(n-1, m-1, d, dp))

  print("Tabulation:", tabulation(n, m))

  print("Space Optmization: ", spaceOptimization(n, m))

gridUniquePathExist(5, 3)