import importlib
import InputMathematics
import numpy as numpy
import re
from PyDictionary import PyDictionary

from ast import literal_eval

def getDataType(inputData = "NOINPUT"):
    tempInput = str(inputData)
    tempReturn = ""
    tempReturnARR = ""
    try:
        if type(inputData) is numpy.ndarray: #fix this if branch
            if isinstance(inputData[0], int):
                tempReturn += "NUMPYLIST,NUM"
                return [tempReturn.split(","), inputData.tolist()]
            elif isinstance(inputData[0], str):
                tempReturn += "NUMPYLIST,STR"
                return [tempReturn.split(","), inputData.tolist()]
            elif isinstance(inputData[0], numpy.ndarray):
                tempReturn += "NUMPYMATRIX,"
                if isinstance(inputData[0][0], int) or isinstance(inputData[0][0], float) or isinstance(inputData[0][0], complex):
                    tempReturn += "NUM"
                    return [tempReturn.split(","), inputData.tolist()]
                elif isinstance(inputData[0][0], str):
                    tempReturn += "STR"
                    return [tempReturn.split(","), inputData.tolist()]
        elif isinstance(inputData,list):
            if isinstance(inputData[0], int) or isinstance(inputData[0], float) or isinstance(inputData[0], complex):
                tempReturn += "LIST,NUM"
                return [tempReturn.split(","), inputData]
            elif isinstance(inputData[0], str):
                tempReturn += "LIST,STR"
                return [tempReturn.split(","), inputData]
            elif isinstance(inputData[0], list):
                tempReturn += "MATRIX,"
                if isinstance(inputData[0][0], int) or isinstance(inputData[0][0], float) or isinstance(inputData[0][0], complex):
                    tempReturn += "NUM"
                    return [tempReturn.split(","), inputData]
                elif isinstance(inputData[0][0], str):
                    tempReturn += "STR"
                    return [tempReturn.split(","), inputData]
        elif len(inputData.split(" ")) > 1:
            tempReturn += "STR"
            return [tempReturn.split(","), inputData]
        elif len(inputData.split(" ")) == 1:
            tempReturn += "STR,WORD"
            return [tempReturn.split(","), inputData]
        else:
            tempReturn = str(type(inputData))
            returnSTR1 = str(tempReturn).find("'")
            returnSTR2 = tempReturn[returnSTR1 + 1: -2] + ","+ tempInput
            return returnSTR2.upper().split(",")
    except (ValueError, SyntaxError):
        return 0

def inputWordCheck(inputData = "NOINPUT"):
    if len(inputData.split(" ")) > 1:
        return 0
    elif len(inputData.split(" ")) == 1:
        dictionary = PyDictionary()
        tempOutput = dictionary.meaning(inputData)
        if tempOutput is 0:
            return 0
        else:
            return 1
    else:
        return 0


def getWordDefinition(inputData = "NOINPUT"):
    dictionary = PyDictionary()
    tempDict = dictionary.meaning(inputData)[next(iter(dictionary.meaning(inputData)))]
    index = 0
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    for str in tempDict:
        tempDict[index] = re.sub(regex, '', str)
        index += 1
    return tempDict

def getWordPartOfSpeech(inputData = "NOINPUT"):
    dictionary = PyDictionary()
    return next(iter(dictionary.meaning(inputData))).upper()

def numpyARRClean(numpyARR):
    return numpyARR.replace("\n ",", ")

def analyzeInput(inputData = "NOINPUT"):
    if inputWordCheck(inputData) == 0:
        return getDataType(inputData)
    else:
        return [getDataType(inputData),getWordDefinition(inputData),getWordPartOfSpeech(inputData)]