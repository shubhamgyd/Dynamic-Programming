
def memoization(ind, N, price, dp):
  if ind == 0:
    return N*price[0]
  
  if dp[ind][N] != -1:
    return dp[ind][N]

  notTake = memoization(ind-1, N, price, dp)
  take = -float('inf')
  rodLength = ind + 1
  if rodLength <= N:
    take = price[ind] + memoization(ind, N-rodLength, price, dp)
  
  dp[ind][N] = max(take, notTake)
  return dp[ind][N]

def tabulation(price):
  n = len(price)
  dp = [[0 for i in range(n+1)] for j in range(n)]
  for N in range(n+1):
    dp[0][N] = N*price[0]
  
  for i in range(1, n):
    for N in range(n+1):
      notTake = dp[i-1][N]
      take = -float("inf")
      rodLength = i + 1
      if rodLength <= N:
        take = price[i] + dp[i][N-rodLength]
      dp[i][N] = max(take, notTake)
  
  return dp[n-1][n]

def cutRod(price):
  n = len(price)
  dp = [[-1 for i in range(n+1)] for j in range(n)]
  print("Prices array:",price)
  print("Memoization:",memoization(n-1, n, price, dp))
  print("Tabulation:",tabulation(price))

testCases = [
  [1, 5, 8, 9, 10, 17, 17, 20],
  [3, 5, 8, 9, 10, 17, 17, 20],
  [1, 10, 3, 1, 3, 1, 5, 9]
]

for prices in testCases:
  cutRod(prices)
