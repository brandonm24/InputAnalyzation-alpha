import sys
import importlib
from importlib import reload
import InputAnalyze
import InputMathematics
import numpy as numpy
from vocabulary.vocabulary import Vocabulary as vb
from InputAnalyze import inputWordCheck
from InputAnalyze import getWordDefinitionPyDict
from InputAnalyze import getWordPartOfSpeech
from InputAnalyze import checkForWordPartOfSpeech
from InputAnalyze import parseInput
from InputAnalyze import analyzeInput
reload(InputAnalyze)
from InputMathematics import NumericMatrixInfo
from InputMathematics import NumericMatrixComparison
from InputMathematics import getMatrixSize
from InputMathematics import NumericMatrixComparison
reload(InputMathematics)

def main():
    print(parseInput(sys.argv[1]))
    return "done"
#    except:
#        print("An error occured, please make sure your input is formatted correctly")


if __name__ == '__main__':
    main()



# def main():
#     try:
#         return analyzeInput(sys.argv[0])
#     except:
#         print("An error occured, please make sure your input is formatted correctly")