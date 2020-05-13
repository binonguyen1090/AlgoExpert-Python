def twoNumberSum(array, targetSum):
    for i in range(len(array)-1):
		fNum = array[i]
		for j in range(i+1,len(array)):
			sNum = array[j]
			if fNum + sNum == targetSum:
				return [fNum, sNum]
    return []
