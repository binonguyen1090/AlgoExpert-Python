# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    result = []


calculate(root, 0, result)
return result


def calculate(node, running_sum, result):
    if node is None:
        return
    newSum = node.value + running_sum
    if (node.left is None and node.right is None):
        result.append(newSum)
        return
    calculate(node.left, newSum, result)
    calculate(node.right, newSum, result)
