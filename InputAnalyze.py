import importlib
import InputMathematics
from InputMathematics import getMatrixSize
from InputMathematics import checkForBinaryList
from InputMathematics import checkForBinaryMatrix
import numpy as numpy
import re
from PyDictionary import PyDictionary

from ast import literal_eval

def analyzeInput(inputData = "NOINPUT"):
    tempInput = str(inputData)
    tempReturn = ""
    try:
        if type(inputData) is numpy.ndarray: #fix this if branch
            if isinstance(inputData[0], int):
                tempReturn += "NUMPYLIST,NUM,"
                if type(inputData) is int:
                    tempReturn += "INT"
                elif type(inputData) is float:
                    tempReturn += "DEC"
                return [tempReturn.split(","), inputData.tolist()]
            elif isinstance(inputData[0], str):
                tempReturn += "NUMPYLIST,STR"
                return [tempReturn.split(","), inputData.tolist()]
            elif isinstance(inputData[0], numpy.ndarray) or isinstance(inputData[0], list):
                tempReturn += "NUMPYMATRIX,"
                if isinstance(inputData[0][0], int) or isinstance(inputData[0][0], float) or isinstance(inputData[0][0], complex):
                    tempReturn += "NUM,"
                    if checkForBinaryMatrix(inputData) == 1:
                        tempReturn += "BINARY"
                    else:
                        tempReturn += "NONBINARY"
                    return [[tempReturn.split(","),getMatrixSize(inputData)], inputData.tolist()]
                elif isinstance(inputData[0][0], str):
                    tempReturn += "STR"
                    return [[tempReturn.split(","),getMatrixSize(inputData)], inputData.tolist()]
        elif type(inputData) is list:
            #if isinstance(inputData[0], int) or isinstance(inputData[0], float) or isinstance(inputData[0], complex):
            if type(inputData[0]) is int or type(inputData[0]) is complex or type(inputData[0]) is float:
                tempReturn += "LIST,NUM,"
                if checkForBinaryList(inputData) is 1:
                    tempReturn += "BINARY,"
                else:
                    tempReturn += "NONBINARY,"
                if type(inputData[0]) is int:
                    tempReturn += "INT"
                elif type(inputData[0]) is float:
                    tempReturn += "DEC"
                return [tempReturn.split(","), inputData]
            elif isinstance(inputData[0], str):
                tempReturn += "LIST,STR"
                return [tempReturn.split(","), inputData]
            elif isinstance(inputData[0], list):
                tempReturn += "MATRIX,"
                if isinstance(inputData[0][0], int) or isinstance(inputData[0][0], float) or isinstance(inputData[0][0], complex):
                    tempReturn += "NUM,"
                    if checkForBinaryMatrix(inputData) == 1:
                        tempReturn += "BINARY"
                    else:
                        tempReturn += "NONBINARY"
                    if type(inputData[0]) is int:
                        tempReturn += "INT"
                    elif type(inputData[0]) is float:
                        tempReturn += "DEC"
                    return [[tempReturn.split(","),getMatrixSize(inputData)], inputData]
                elif isinstance(inputData[0][0], str):
                    tempReturn += "STR"
                    return [[tempReturn.split(","),getMatrixSize(inputData)], inputData]
        elif type(inputData) is int:
            tempReturn += "NUM,INT"
            return [tempReturn.split(","), inputData]
        elif type(inputData) is float:
            tempReturn += "NUM,DEC"
            return [tempReturn.split(","), inputData]
        elif len(inputData.split(" ")) > 1:
            if inputWordCheckMultiple(inputData) == 1:
                tempReturn += "STR,PHRASE"
                tempARR1 = [inputData, inputData.split(" "), getWordPartOfSpeechMultiple(inputData.split(" "))]
                tempARR2 = getWordDefinitionPyDictMultiple(inputData)
                tempARR3 = getMatrixSize([tempARR1,tempARR2])
                return [[tempReturn.split(","),tempARR3],[tempARR1, tempARR2]]
            else:
                tempReturn += "STR"
                return [[tempReturn],inputData]
        elif len(inputData.split(" ")) == 1:
            if inputWordCheck(inputData) == 1:
                tempReturn += "STR,WORD"
                return [tempReturn.split(","), [inputData,getWordPartOfSpeech(inputData)], getWordDefinitionPyDict(inputData)]
            else:
                tempReturn += "STR"
                return [tempReturn, inputData]
        else:
            tempReturn = str(type(inputData))
            returnSTR1 = str(tempReturn).find("'")
            returnSTR2 = tempReturn[returnSTR1 + 1: -2] + ","+ tempInput
            return returnSTR2.upper().split(",")
    except (ValueError, SyntaxError):
        return 0

def inputWordCheck(inputData = "NOINPUT"):
    if len(inputData.split(" ")) > 1:
        return inputWordCheckMultiple(inputData)
    elif len(inputData.split(" ")) == 1:
        dictionary = PyDictionary()
        tempOutput = dictionary.meaning(inputData)
        if tempOutput is 0:
            return 0
        else:
            return 1
    else:
        return 0

def inputWordCheckMultiple(inputData="NOINPUT"):
    tempOutput = 0
    tempARR = inputData.split(" ")
    for str in tempARR:
        dictionary = PyDictionary()
        tempOutput = dictionary.meaning(str)
        if tempOutput is 0:
            tempOutput = 0
            break
        else:
            tempOutput = 1
    return tempOutput


def getWordDefinitionPyDictMultiple(inputData = "NOINPUT"):
    tempARR = inputData.split(" ")
    index = 0
    tempDict = ""
    for word in tempARR:
        tempDict = getWordDefinitionPyDict(word)
        tempARR[index] = [tempDict]
        index += 1
    return tempARR

def getWordPartOfSpeech(inputData = "NOINPUT"):
    dictionary = PyDictionary()
    if checkForWordPartOfSpeech(inputData, "Adjective") == 1:
        wordDef = dictionary.meaning(inputData)
        keys = list(wordDef.keys())
        if len(keys) > 1:
            return ["Adjective",keys[1]]
        else:
            return ["Adjective"]
    elif checkForWordPartOfSpeech(inputData, "Verb") == 1:
        wordDef = dictionary.meaning(inputData)
        keys = list(wordDef.keys())
        if len(keys) > 1:
            return ["Verb",keys[1]]
        else:
            return ["Verb"]
    elif checkForWordPartOfSpeech(inputData, "Noun") == 1:
        wordDef = dictionary.meaning(inputData)
        keys = list(wordDef.keys())
        if len(keys) > 1:
            return ["Noun",keys[1]]
        else:
            return ["Noun"]
    else:
        return next(iter(dictionary.meaning(inputData))).upper()

def getWordPartOfSpeechMultiple(inputData = "NOINPUT"):
    tempList = list()
    for word in inputData:
        tempList.append(getWordPartOfSpeech(word))
    return tempList

def getWordDefinitionPyDict(inputData = "NOINPUT"):
    dictionary = PyDictionary()
    index = 0
    indexInner = 0
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if len(getWordPartOfSpeech(inputData)) > 1:
        tempDict = [dictionary.meaning(inputData)[getWordPartOfSpeech(inputData)[0]], dictionary.meaning(inputData)[getWordPartOfSpeech(inputData)[1]]]
        for definition in tempDict:
            for str in definition:
                tempDict[index][indexInner] = re.sub(regex, '', str)
                indexInner += 1
            index += 1
            indexInner = 0
    else:
        tempDict = dictionary.meaning(inputData)[getWordPartOfSpeech(inputData)[0]]
        for str in tempDict:
            tempDict[index] = re.sub(regex, '', str)
            index += 1
    return tempDict


def checkForWordPartOfSpeech(word, key, dictionary = PyDictionary()):
    wordDef = dictionary.meaning(word)
    keys = list(wordDef.keys())
    if key in keys:
        if keys.index(key) == 0:
            return 1
        else:
            return 0
    else:
        return 0

def numpyARRClean(numpyARR):
    return numpyARR.replace("\n ",", ")

def parseInput(inputData="NOINPUT"):
    if inputData.startswith('[') and inputData.endswith(']'):
        #return map(type(inputData.strip('[]').split(',')[0]), inputData.strip('[]').split(','))
        return strToMatrixOrList(inputData)
    else:
        if inputData.isdigit():
            return int(inputData)
        elif inputData.count('.') is 1:
            return float(inputData)
        else:
            return inputData

def strToMatrixOrList(inputData="NOINPUT"):
    if inputData.startswith('[') and inputData.endswith(']'):
        if inputData.count('[') > 1 and inputData.count(']') > 1:
            #return [strToMatrixOrList(item) for item in inputData.split(",")]
            return inputData.strip('[]').split(' ')
        elif inputData.count('[') is 1 and inputData.count(']') and 1:
            if inputData.strip('[]').split(',')[0].isdigit():
                return [int(s) for s in inputData.strip('[]').split(',')]
            elif inputData.strip('[]').split(',')[0].count('.') is 1:
                return [float(s) for s in inputData.strip('[]').split(',')]
            else:
                return inputData.strip('[]').split(',')
    else:
        if type(inputData) is int:
            return int(inputData)
        elif type(inputData) is float:
            return float(inputData)
        else:
            return inputData
    