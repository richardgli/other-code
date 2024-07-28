def hasPathSum(tree_list, targetSum):
  if not tree_list:
    return False
  #instead of storing the value, store the index so that each node is unique
  frontier = [[0, tree_list[0]]] #[index, current sum from root ot the current node]

  while frontier:
    cur = frontier.pop()
    index = cur[0]
    cur_sum = cur[1]
    leftIndex = index * 2 + 1
    rightIndex = index * 2 + 2

    if tree_list[leftIndex] == None and tree_list[rightIndex] == None:
      if cur_sum == targetSum:
        return True

    if tree_list[leftIndex]:
      frontier.append([leftIndex, cur_sum + tree_list[leftIndex]])

    if tree_list[rightIndex]:
      frontier.append([rightIndex, cur_sum + tree_list[rightIndex]])

  return False
