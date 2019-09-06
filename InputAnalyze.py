import importlib
import InputMathematics
import numpy as numpy
from PyDictionary import PyDictionary

from ast import literal_eval

def getDataType(inputData = "NOINPUT"):
    tempInput = str(inputData)
    tempReturn = ""
    try:
        if type(inputData) is numpy.ndarray:
            if isinstance(inputData[0], int):
                tempReturn += "NUMPYLIST,NUM," + tempInput
            elif isinstance(inputData[0], str):
                tempReturn += "NUMPYLIST,STR," + tempInput
            elif isinstance(inputData[0], numpy.ndarray):
                tempReturn += "NUMPYMATRIX,"
                if isinstance(inputData[0][0], int) or isinstance(inputData[0][0], float) or isinstance(inputData[0][0], complex):
                    tempReturn += "NUM," + tempInput
                elif isinstance(inputData[0][0], str):
                    tempReturn += "STR," + tempInput
            tempReturnARR = tempReturn.split(",")
            index = 0
            for string in tempReturnARR:
                tempReturnARR[index] = string.replace("'[[","[[")
                tempReturnARR[index] = string.replace(" ' ","")
                tempReturnARR[index] = string.replace("\n ",", ")
                index += 1
            return tempReturnARR
        elif isinstance(inputData,list):
            if isinstance(inputData[0], int) or isinstance(inputData[0], float) or isinstance(inputData[0], complex):
                tempReturn += "LIST , NUM , " + tempInput
            elif isinstance(inputData[0], str):
                tempReturn += "LIST , STR , " + tempInput
            elif isinstance(inputData[0], list):
                tempReturn += "MATRIX , "
                if isinstance(inputData[0][0], int) or isinstance(inputData[0][0], float) or isinstance(inputData[0][0], complex):
                    tempReturn += "NUM , " + tempInput
                elif isinstance(inputData[0][0], str):
                    tempReturn += "STR , " + tempInput
            tempReturnARR = tempReturn.split(" , ")
            index = 0
            for string in tempReturnARR:
                tempReturnARR[index] = string.replace("'","").replace("\n ", "")
                index += 1
            return tempReturnARR
        else:
            tempReturn = str(type(inputData))
            returnSTR1 = str(tempReturn).find("'")
            returnSTR2 = tempReturn[returnSTR1 + 1: -2] + ","+ tempInput
            return returnSTR2.upper()
    except (ValueError, SyntaxError):
        return str


def inputInfo(inputData = "NOINPUT"):
    if not inputData.any() or not inputData.all():
        return "NOINPUT"
    elif inputData.endswith(".exe") or inputData.endswith(".txt"):
        return "FILE" + "," + str(inputData)
    else:
        returnSTR = str(getDataType(inputData))
        returnSTR1 = str(returnSTR).find("'")
        returnSTR2 = returnSTR[returnSTR1: -1]
        return returnSTR2.replace("'","").upper() + "," + str(inputData)

def inputWordCheck(inputData = "NOINPUT"):
    dictionary = PyDictionary()
    try:
        tempOutput = dictionary.meaning(inputData, disable_errors=True)
    except:
        return 0
    else:
        return 1
