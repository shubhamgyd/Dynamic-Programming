
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

def gridUniquePathExist(n, m):

  d = [(-1, 0), (0, -1)]
  # print(recursive(n-1, m-1, d))

  dp = [[-1 for i in range(m)] for i in range(n)]
  print(memoization(n-1, m-1, d, dp))

gridUniquePathExist(3, 2)