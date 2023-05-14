import pathlib
def mainPath():
	return pathlib.Path().resolve()
def dataPath():
	return mainPath().joinpath('HospitalManager').joinpath('Static').joinpath('databases')