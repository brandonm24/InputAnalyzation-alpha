import importlib
import InputMathematics
from InputMathematics import getMatrixSize
from InputMathematics import checkForBinaryList
from InputMathematics import checkForBinaryMatrix
import numpy as numpy
import re
from PyDictionary import PyDictionary

# def numpyARRClean(numpyARR):
#     return numpyARR.replace("\n ",", ")

def parseInput(inputData="NOINPUT"):
    if inputData.startswith('[') and inputData.endswith(']'):
        return strToMatrixOrList(inputData)
    else:
        if inputData.isdigit() and type(inputData) is int:
            return int(inputData)
        elif inputData.count('.') is 1 and type(inputData) is float :
            return float(inputData)
        else:
            return inputData

def strToMatrixOrList(inputData="NOINPUT"):
    if inputData.startswith('[') and inputData.endswith(']'):
        if inputData.count('[') is 1 and inputData.count(']') and 1:
            return strToListConversion(inputData)
        elif inputData.count('[') > 1 and inputData.count(']') > 1:
            return strToMatrixConversion(inputData)

def strToListConversion(inputMatrixSTR):
    tempReturnMatrix = []
    tempSTR = ""
    for string in inputMatrixSTR.split(","):
        tempSTR = string.replace("[", "").replace("]", "")
        if tempSTR.isdigit():
            tempReturnMatrix.append(int(tempSTR))
        elif tempSTR.count(".") is 1:
            tempReturnMatrix.append(float(tempSTR))
        elif type(tempSTR) is str and tempSTR is not ',' and tempSTR is not '[' and tempSTR is not ']':
            tempReturnMatrix.append(tempSTR)
        elif tempSTR is ']':
            break
    return tempReturnMatrix


def strToMatrixConversion(inputMatrixSTR, ):
    inputMatrix = inputMatrixSTR
    tempReturnMatrix = []
    tempInnerMatrix = []
    tempInnerMatrix2 = []
    tempSTR = ""
    inputMatrix = inputMatrix.strip("[").strip("]").split(";")
    for string in inputMatrix:
        tempSTR = string.strip().replace(" ", "").replace("[", "").replace("]", "")
        tempInnerMatrix = tempSTR.split(",")
        for char in tempInnerMatrix:
            if char.isdigit():
                tempInnerMatrix2.append(int(char))
            elif char.count(".") is 1:
                tempInnerMatrix2.append(float(char))
            elif type(char) is str and char is not ',' and char is not '[' and char is not ']':
                tempInnerMatrix2.append(char)
        tempReturnMatrix.append(tempInnerMatrix2)
        tempInnerMatrix2 = []
    return tempReturnMatrix
