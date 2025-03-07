
def recursion(ind, arr):
  if ind == 0:
    return 0
  
  left = recursion(ind-1, arr) + abs(arr[ind] - arr[ind-1])

  right = float("inf")
  if ind > 1:
    right = recursion(ind-2, arr) + abs(arr[ind] - arr[ind-2])
  
  return min(left, right)
def memoization(ind, arr, dp):
  if ind == 0:
    return 0
  
  if dp[ind] != -1:
    return dp[ind]
  
  left = memoization(ind-1, arr, dp) + abs(arr[ind] - arr[ind-1])

  right = float("inf")
  if ind > 1:
    right = memoization(ind-2, arr, dp) + abs(arr[ind] - arr[ind-2])
  
  dp[ind] = min(left, right)
  return dp[ind]

def tabulation(arr):
  n = len(arr)
  dp = [0 for i in range(n)]
  for i in range(1, n):
    left = dp[i-1] + abs(arr[i] - arr[i-1])
    right = float("inf")
    if i > 1:
      right = dp[i-2] + abs(arr[i] - arr[i-2])
    dp[i] = min(left, right)
  return dp[n-1]

def frogJump(arr):
  n = len(arr)-1
  # return recursion(n, arr)
  dp = [-1 for i in range(len(arr))]
  return memoization(n, arr, dp)
  # return tabulation(arr)

# arr = [20, 30, 40, 20]
arr = [30, 20, 50, 10, 40]
print(frogJump(arr))