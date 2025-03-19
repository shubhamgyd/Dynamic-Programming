
def recursive(ind, capacity, val , wt):
  if ind == 0:
    if capacity >= wt[0]:
      return val[0]
    return 0
  
  pick = 0
  if capacity >= wt[ind]:
    pick = val[ind] + recursive(ind-1, capacity-wt[ind], val, wt)
  
  notPick = recursive(ind-1, capacity, val, wt)

  return max(pick, notPick)

def memoization(ind, capacity, val , wt, dp):
  if ind == 0:
    if capacity >= wt[0]:
      return val[0]
    return 0
  
  if dp[ind][capacity] != -1:
    return dp[ind][capacity]
  
  pick = 0
  if capacity >= wt[ind]:
    pick = val[ind] + memoization(ind-1, capacity-wt[ind], val, wt, dp)
  
  notPick = memoization(ind-1, capacity, val, wt, dp)

  dp[ind][capacity] = max(pick, notPick)
  return dp[ind][capacity]

def tabulation(val, wt, capacity, N):
  dp = [[0 for i in range(capacity+1)] for j in range(N)]
  for i in range(capacity+1):
    if wt[0] <= i:
      dp[0][i] = val[0]
  
  for i in range(1, N):
    for cp in range(1, capacity+1):
      pick = 0
      if cp >= wt[i]:
        pick = val[i] + dp[i-1][cp-wt[i]]
      notPick = dp[i-1][cp]

      dp[i][cp] = max(pick, notPick)
  
  return dp[N-1][capacity]

def spaceOptimization(val, wt, capacity, N):
  prev = [0 for i in range(capacity+1)]
  cur = [0 for i in range(capacity+1)]
  for i in range(capacity+1):
    if wt[0] <= i:
      prev[i] = val[0]
  
  for i in range(1, N):
    for cp in range(1, capacity+1):
      pick = 0
      if cp >= wt[i]:
        pick = val[i] + prev[cp-wt[i]]
      notPick = prev[cp]

      cur[cp] = max(pick, notPick)
    prev = cur.copy()
  
  return prev[capacity]

def singleArraySpaceOptimization(val, wt, capacity, N):
  prev = [0 for i in range(capacity+1)]
  for i in range(capacity+1):
    if wt[0] <= i:
      prev[i] = val[0]
  
  for i in range(1, N):
    for cp in range(capacity, 0, -1):
      pick = 0
      if cp >= wt[i]:
        pick = val[i] + prev[cp-wt[i]]
      notPick = prev[cp]

      prev[cp] = max(pick, notPick)
  
  return prev[capacity]

def knapsack(val, wt, capacity):
  N = len(val)
  print("Recursive", recursive(N-1, capacity, val, wt))
  dp = [[-1 for i in range(capacity+1)] for j in range(N)]
  print("Memoization:", memoization(N-1, capacity, val, wt, dp))
  print("Tabulation:", tabulation(val, wt, capacity, N))
  print("SpaceOptimization:", spaceOptimization(val, wt, capacity, N))
  print("Single Array Optimization:", singleArraySpaceOptimization(val, wt, capacity, N))


testCases = [
{
  "val": [6, 1, 7, 7],
  "wt": [1, 3, 4, 5],
  "capacity": 8
},
{
  "val": [1, 1],
  "wt": [2, 1],
  "capacity": 3
},
{
  "val": [6, 8, 7, 100],
  "wt": [2, 3, 4, 5],
  "capacity": 15
}
]
for tc in testCases:
  knapsack(tc["val"], tc["wt"], tc["capacity"])
  