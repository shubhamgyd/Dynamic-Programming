
def recursion(last, day, days):
  if day == 0:
    maxi = 0
    for i in range(3):
      if i != last:
        maxi = max(maxi, days[day][i])
    return maxi
  
  res = 0
  for i in range(3):
    if i != last:
      res = max(res, days[day][i] + recursion(i, day-1, days))
  return res

def memoization(last, day, days, dp):
  if day == 0:
    maxi = 0
    for i in range(3):
      if i != last:
        maxi = max(maxi, days[day][i])
    return maxi
  
  if dp[day][last] != -1:
    return dp[day][last]
  
  res = 0
  for i in range(3):
    if i != last:
      res = max(res, days[day][i] + memoization(i, day-1, days, dp))
  dp[day][last] = res
  return dp[day][last]

def tabulation(N, days):
  dp = [[0 for i in range(4)] for i in range(N)]

  dp[0][0] = max(days[0][1], days[0][2])
  dp[0][1] = max(days[0][0], days[0][2])
  dp[0][2] = max(days[0][0], days[0][1])
  dp[0][3] = max(days[0][0], days[0][1], days[0][2])
  
  for day in range(1, N):
    for last in range(4):
      res = 0
      for i in range(3):
        if i != last:
          res = max(res, days[day][i] + dp[day-1][i])
      dp[day][last] = res
  
  return dp[N-1][3]

def spaceOptimization(N, days):
  prev = [0 for i in range(4)]
  prev[0] = max(days[0][1], days[0][2])
  prev[1] = max(days[0][0], days[0][2])
  prev[2] = max(days[0][0], days[0][1])
  prev[3] = max(days[0][0], days[0][1], days[0][2])

  for day in range(1, N):
    temp = [0 for i in range(4)]
    for last in range(4):
      res = 0
      for i in range(3):
        if i != last:
          res = max(res, days[day][i] + prev[i])
      temp[last] = res
    prev = temp.copy()
  
  return prev[3]

if __name__=="__main__":
  T = int(input())
  while T:
    N = int(input())
    days = []
    for i in range(N):
      days.append(list(map(int, input().strip().split())))
    # print(recursion(-1, N-1, days))
    # dp = [[-1 for i in range(4)] for i in range(N)]
    # print(memoization(3, N-1, days, dp))
    # print(tabulation(N, days))
    print(spaceOptimization(N, days))
    T -= 1

'''
Test case:
3
1 2 5
3 1 1
3 3 3
11
3
10 40 70
20 50 80
30 60 90
210
'''