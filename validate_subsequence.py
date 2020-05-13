def isValidSubsequence(array, sequence):
        aInd = 0
        sInd = 0
        while aInd < len(array) and sInd < len(sequence):
            if array[aInd] == sequence[sInd]:
                    sInd += 1
                aInd += 1

        return sInd == len(sequence)
