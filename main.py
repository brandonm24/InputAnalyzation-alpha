import importlib
from importlib import reload
import InputAnalyze
import InputMathematics
import numpy as numpy
from InputAnalyze import getDataType
from InputAnalyze import inputWordCheck
from InputAnalyze import getWordDefinition
from InputAnalyze import getWordPartOfSpeech
from InputAnalyze import analyzeInput
reload(InputAnalyze)
from InputMathematics import NumericMatrixInfo
from InputMathematics import NumericMatrixComparison
from InputMathematics import NumericMatrixInfo
from InputMathematics import NumericMatrixComparison
reload(InputMathematics)




a = [[1,2,4,5,6,67,8,6],[1]]
#print(inputWordCheck("zebras are"))
# print(getDataType("salamander"))
# print(getWordDefinition("salamander"))
# print(getWordPartOfSpeech("salamander"))
#print(NumericMatrixInfo([[1,2,4,5,6,67,8,6],[2,2,4,5,6,67,8,6],[1,2,3]]))
print(analyzeInput("good"))