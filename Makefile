main: AnalyzePy InputAnalyzePy InputMathematicsPy InputOrientationPy

AnalyzePy: analyze.py
	python -m py_compile analyze.py

InputAnalyzePy: InputAnalyze.py
	python -m py_compile InputAnalyze.py

InputMathematicsPy: InputMathematics.py
	python -m py_compile InputMathematics.py

InputOrientationPy: InputOrientation.py
	python -m py_compile InputOrientation.py