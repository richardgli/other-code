def evenList(list):
  if not list:
    return list

  newList = evenList(list[:len(list) - 1])

  if list[-1] % 2 == 0:
      newList.append(list[-1])
  return newList
