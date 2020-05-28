def bubbleSort(array):
    sorted = False


while not sorted:
		sorted = True

		for i in range(0, len(array)-1):
			j = i + 1
			if (array[i] > array[j]):
				array[i], array[j] = array[j], array[i]
				sorted = False

	return (array)
