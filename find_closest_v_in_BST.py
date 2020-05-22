def findClosestValueInBst(tree, target):
	closest = float("inf")
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.right
        elif target > currentNode.value:
            currentNode = currentNode.left
        else:
            break

    return closest
