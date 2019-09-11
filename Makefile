main: InputAnalyzePy InputMathematicsPy AnalyzePy

InputAnalyzePy: InputAnalyze.py
	python -m py_compile InputAnalyze.py

AnalyzePy: analyze.py
	python -m py_compile analyze.py

InputMathematicsPy: InputMathematics.py
	python -m py_compile InputMathematics.py
