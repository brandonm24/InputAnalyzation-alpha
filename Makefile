main: InputAnalyzePy InputMathematicsPy mainPy

InputAnalyzePy: InputAnalyze.py
	python InputAnalyze.py

mainPy: main.py
	python main.py

InputMathematicsPy: InputMathematics.py
	python InputMathematics.py
