def twoNumberSum(array, targetSum):
	answerArray = []
    for i in array:
		for j in array:
			if i + j == targetSum and i != j and i not in answerArray:
				answerArray.append(i)
				answerArray.append(j)
				break
	return(answerArray)
    pass
