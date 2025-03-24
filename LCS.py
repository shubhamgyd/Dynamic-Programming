def memoization(ind1, ind2, s, t, dp):
  if ind1 < 0 or ind2 < 0:
    return 0
  
  if dp[ind1][ind2] != -1:
    return dp[ind1][ind2]
  
  if s[ind1] == t[ind2]:
    dp[ind1][ind2] = 1 + memoization(ind1-1, ind2-1, s, t, dp)
    return dp[ind1][ind2]
  
  dp[ind1][ind2] = max(memoization(ind1-1, ind2, s, t, dp), memoization(ind1, ind2-1, s, t, dp))
  return dp[ind1][ind2]

def tabulation(s, t):
  n, m = len(s), len(t)
  dp = [[0 for i in range(m+1)] for j in range(n+1)]

  for i in range(1, n+1):
    for j in range(1, m+1):
      if s[i-1] == t[j-1]:
        dp[i][j] = 1 + dp[i-1][j-1]
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
  return dp[n][m]

def spaceOptimization(s, t):
  n, m = len(s), len(t)
  prev = [0 for i in range(m+1)]
  cur = [0 for i in range(m+1)]

  for i in range(1, n+1):
    for j in range(1, m+1):
      if s[i-1] == t[j-1]:
        cur[j] = 1 + prev[j-1]
      else:
        cur[j] = max(prev[j], cur[j-1])
    prev = cur.copy()
  return prev[m]

def lcs(s, t):
  n = len(s)
  m = len(t)
  dp = [[-1 for i in range(m)] for j in range(n)]
  print("Memoization:", memoization(n-1, m-1, s, t, dp))
  print("Tabulation:", tabulation(s, t))
  print("SpaceOptimization:", spaceOptimization(s, t))

s = "aedfg"
t = "caedg"
lcs(s, t)