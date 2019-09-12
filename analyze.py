import sys
import importlib
from importlib import reload
import InputAnalyze
import InputMathematics
import InputOrientation
import numpy as numpy
from vocabulary.vocabulary import Vocabulary as vb
from InputAnalyze import inputWordCheck
from InputAnalyze import getWordDefinitionPyDict
from InputAnalyze import getWordPartOfSpeech
from InputAnalyze import checkForWordPartOfSpeech
from InputAnalyze import analyzeInput
reload(InputAnalyze)
from InputMathematics import NumericMatrixInfo
from InputMathematics import NumericMatrixComparison
from InputMathematics import getMatrixSize
from InputMathematics import NumericMatrixComparison
reload(InputMathematics)
from InputOrientation import parseInput
from InputOrientation import strToMatrixOrList

def main():
    print(analyzeInput(parseInput(sys.argv[1])))


if __name__ == '__main__':
    main()