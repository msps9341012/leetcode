def paths_with_sum(binary_tree, target_sum):
  partial_paths = ListDict({target_sum: [[]]})
  return paths_with_partial_sum(binary_tree, target_sum, partial_paths)
  
def paths_with_partial_sum(node, target_sum, partial_paths):
  if not node:
    return []
  next_partial_paths = ListDict({target_sum: [[]]})
  for path_sum, paths in partial_paths.items():
    for path in paths:
      next_partial_paths[path_sum - node.value] += [path + [node.name]]
  paths = next_partial_paths[0]
  for child in [node.left, node.right]:
    paths += paths_with_partial_sum(child, target_sum, next_partial_paths)
  return paths

class Node():
  def __init__(self, name, value, left=None, right=None):
    self.name, self.value, self.left, self.right = name, value, left, right

class ListDict(dict):
  def __missing__(self, key):
    return []



bt=Node("A",4,Node("B",-2,Node("D",7),Node("E", 4)),
              Node("C", 7,Node("F",-1,Node("H",-1),Node("I",2,Node("K",1)))))


print(paths_with_sum(bt, 2))
