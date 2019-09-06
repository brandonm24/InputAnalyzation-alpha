import importlib
from importlib import reload
import InputAnalyze
import InputMathematics
import numpy as nump
from InputAnalyze import inputInfo
from InputAnalyze import getDataType
from InputAnalyze import inputWordCheck
reload(InputAnalyze)
from InputMathematics import NumericMatrixInfo
from InputMathematics import NumericMatrixComparison
from InputMathematics import NumericMatrixInfo
from InputMathematics import NumericMatrixComparison
reload(InputMathematics)




a = [[2,2,4,5,6,67,8,6],[1,2,3]]
print(inputWordCheck("greetings"))
print(getDataType("greetings"))
#print(NumericMatrixInfo([[1,2,4,5,6,67,8,6],[2,2,4,5,6,67,8,6],[1,2,3]]))
