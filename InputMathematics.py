
import importlib
import array as arr
import numpy as nump






def NumericMatrixInfo(inputMatrix):
    matrixLength = 0  #outputARR[0]
    matrixMinWidth = 0 #outputARR[1]
    matrixMaxWidth = 0 #outputARR[2]
    matrixSum = 0 #outputARR[3]
    matrixTotalNumbers = 0 #outputARR[4]
    smallestNumber = 0 #outputARR[5]
    largestNumber = 0 #outputARR[6]
    outputSTR = ""
    outputARR = [0, 0, 0, 0, 0, 0, 0, 0]
    for row in inputMatrix:
        matrixLength += 1
        matrixTotalNumbers += len(row)
        if(matrixMaxWidth == 0 and matrixMinWidth ==0):
            matrixMaxWidth = len(row)
            matrixMinWidth = len(row)
            smallestNumber = row[0]
            largestNumber = row[0]
        if(len(row) > matrixMaxWidth):
            matrixMaxWidth = len(row)
        elif(len(row) < matrixMinWidth):
            matrixMinWidth = len(row)
        for number in row:
            matrixSum += number
            # if number == 0:
            #     smallestNumber = number
            if largestNumber < number:
                largestNumber = number
            elif number < smallestNumber:
                smallestNumber = number
    outputSTR += "Matrix Length: " + str(matrixLength) + "\n"
    outputARR[0] = matrixLength
    outputSTR += "Min Matrix Width: " + str(matrixMinWidth) + "\n"
    outputARR[1] = matrixMinWidth
    outputSTR += "Max Matrix Width: " + str(matrixMaxWidth) + "\n"
    outputARR[2] = matrixMaxWidth
    outputSTR += "Matrix Sum: " + str(matrixSum) + "\n"
    outputARR[3] = matrixSum
    outputSTR += "Total Matrix Numbers: " + str(matrixTotalNumbers) + "\n"
    outputARR[4] = matrixTotalNumbers
    outputSTR += "Smallest Number: " + str(smallestNumber) + "\n"
    outputARR[5] = smallestNumber
    outputSTR += "Largest Number: " + str(largestNumber) + "\n"
    outputARR[6] = largestNumber
    outputSTR += "Average: " + str(matrixSum / matrixTotalNumbers) + "\n" #outputARR[7]
    outputARR[7] = matrixSum / matrixTotalNumbers
    print(outputSTR)
    return outputARR

def NumericMatrixComparison(inputMatrix1, inputMatrix2, comparisonCode=0):
    tempARR1 = NumericMatrixInfo(inputMatrix1)
    tempARR2 = NumericMatrixInfo(inputMatrix2)
    if(tempARR1[comparisonCode] > tempARR2[comparisonCode]):
        return 1
    elif(tempARR1[comparisonCode] < tempARR2[comparisonCode]):
        return 2
    elif(tempARR1[comparisonCode] == tempARR2[comparisonCode]):
        return 0
