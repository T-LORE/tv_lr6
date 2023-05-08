import numpy as np

#перечисление рядов (частот, относительныйх частот)

class RowType:
    FREQUENCY = 1
    RELATIVE_FREQUENCY = 2

def getVariationRow(numbersArray):
    sortedArray = np.sort(numbersArray)
    return sortedArray


def getFrequencyRow(numbersArray, type : RowType):
    if type == RowType.FREQUENCY:
        frequencyRow = {
            "numbers" : np.unique(numbersArray, return_counts=True)[0],
            "frequencies" : np.unique(numbersArray, return_counts=True)[1]   
        }
        return frequencyRow
    elif type == RowType.RELATIVE_FREQUENCY:
        relativeFrequencyRow = {
            "numbers" : np.unique(numbersArray, return_counts=True)[0],
            "numerators" : np.unique(numbersArray, return_counts=True)[1],
            "denominator" : len(numbersArray)
        }
        return relativeFrequencyRow
    else:
        raise ValueError("Неверный тип ряда")
    
#характеристик выборки: X выборочное, D выборочное, сигма выборочное, S

def getX(numbersArray):
    return np.mean(numbersArray)

#выборочная дисперсия
def getD(numbersArray):
    return np.var(numbersArray)

#выборочное среднее квадратическое отклонение
def getSigma(numbersArray):
    return np.std(numbersArray)

def getS(numbersArray):
    return np.sqrt(getD(numbersArray))

