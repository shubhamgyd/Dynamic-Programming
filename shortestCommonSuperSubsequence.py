def shortestCommonSuperSubsequence(s1, s2):
  dp = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]

  for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
      if s1[i-1] == s2[j-1]:
        dp[i][j] = 1 + dp[i-1][j-1]
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
  
  ans = ""
  i = len(s1)
  j = len(s2)
  while i > 0 and j > 0:
    if s1[i-1] == s2[j-1]:
      ans += s1[i-1]
      i -= 1
      j -= 1
    else:
      if dp[i-1][j] > dp[i][j-1]:
        ans += s1[i-1]
        i -= 1>>>
      else:
        ans += s2[j-1]
        j -= 1
  while j > 0:
    ans += s2[j-1]
    j -= 1
  while i > 0:
    ans += s1[i-1]
    i -= 1
  return ans[::-1]

testcases = [
  ["brute", "single"],
  ["bleed", "blue"]
]

for tc in testcases:
  s1, s2 = tc
  print(f"Shortest Common Subsequence for '{s1}' and '{s2}' is {shortestCommonSubsequence(s1, s2)}")