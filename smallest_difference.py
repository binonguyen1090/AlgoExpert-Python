def smallestDifference(arrayOne, arrayTwo):
	arrayOne.sort()
	arrayTwo.sort()
    index1 = 0
	index2 = 0
	smallest = float("inf")
	currentDifferent = float("inf")
	result = []
	while index1 < len(arrayOne) and index2 < len(arrayTwo):
		firstN = arrayOne[index1]
		secondN = arrayTwo[index2]
		if firstN < secondN:
			currentDifferent = secondN - firstN
			index1 += 1
		elif firstN > secondN:
			currentDifferent = firstN - secondN
			index2 += 1
		else:
			return [firstN,secondN]
		if currentDifferent < smallest:
			smallest = currentDifferent
			result = [firstN,secondN]
    return result
