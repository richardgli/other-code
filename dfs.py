'''
Given a collection of distinct integers, return all possible permutations.
Example:
Input: [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
'''

def receive():
  nums = list(map(int, input().split()))
  visited = [False] * len(nums)
  path =[]
  res = []
  print(dfs(path, visited, res, nums))


def dfs(path, visited, res, nums):

  if len(path) == len(nums):
    res.append(path.copy())
    return res

  for i in range(len(nums)):

    if (nums[i] not in path) and (visited[i] == False):
      path.append(nums[i])
      visited[i] = True
      res = dfs(path, visited, res, nums)
      visited[i] = False
      path.pop()
  return res
  
receive()



