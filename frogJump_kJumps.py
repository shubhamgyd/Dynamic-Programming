
def recursion(ind, arr, k):
  if ind == 0:
    return 0
  
  result = float("inf")
  for i in range(1, k+1):
    step = float('inf')
    if (ind > (i-1)):
      step = recursion(ind-i, arr, k) + abs(arr[ind] - arr[ind-i])
    result = min(result, step)
  return result
def frogJumpK(arr, k):
  return recursion(len(arr)-1, arr, k)

arr = [30, 20, 50, 10, 40]
print(frogJumpK(arr, 4))