def isMonotonic(array):
    isNoneIncreasing = True
    isNoneDecreasing = True
	for i in range(1, len(array)):
		if array[i] > array[i-1]:
			isNoneIncreasing = False
		if array[i] < array[i-1]:
			isNoneDecreasing = False
    return isNoneIncreasing or isNoneDecreasing
