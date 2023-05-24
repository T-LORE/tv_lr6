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
    return (1/len(numbersArray)) * np.sum(numbersArray)

#выборочная дисперсия
def getD(numbersArray):
    return np.var(numbersArray)

#выборочное среднее квадратическое отклонение
def getSigma(numbersArray):
    return np.sqrt(getD(numbersArray))

def getS(numbersArray):
    return (1/(len(numbersArray) - 1)) * np.sum(numbersArray )


#Разбить на минимальное количество интервалов, чтобы частота каждого интервала была не меньше заданной
def split_array_into_intervals(arr, min_frequency):
    arr = np.sort(arr)
    intervals = {
        'start' : [],
        'end' : [],
        'frequency' : []
    }
    current_interval = [arr[0],0]
    current_in_interval = [arr[0]]
    frequency = 0

    for num in arr:
        if frequency < min_frequency:
            if ((len(intervals['start']) == 0) and (num >= current_interval[0])) or ((len(intervals['start']) > 0) and (num > current_interval[0])):
                frequency+=1
                current_in_interval.append(num)
        else:
            if num in current_in_interval:
                frequency+=1
                current_in_interval.append(num)
            else:
                if current_interval[0] == current_in_interval[-1]:
                    frequency+=1
                    current_in_interval.append(num)
                else:
                    current_interval[1] = current_in_interval[-1]
                    intervals['start'].append(current_interval[0])
                    intervals['end'].append( current_interval[1])
                    intervals['frequency'].append(frequency)
                    current_interval[0] = current_in_interval[-1]
                    frequency = 1
                    current_in_interval.append(num)
    if frequency >= min_frequency:
        current_interval[1] = current_in_interval[-1]
        intervals['start'].append(current_interval[0])
        intervals['end'].append( current_interval[1])
        intervals['frequency'].append(frequency)
    else:
        intervals['end'][-1] = current_in_interval[-1]
        intervals['frequency'][-1] += frequency

    return intervals

#Объеденить 2 интервала с минимальной частотой
def min_sum(arr):
    min_sum = float('inf')
    min_index = -1

    for i in range(len(arr['start']) - 1):
        current_sum = arr['frequency'][i] + arr['frequency'][i + 1]
        if current_sum < min_sum:
            min_sum = current_sum
            min_index = i

    if min_index != -1:
        new_value = arr['frequency'][min_index] + arr['frequency'][min_index + 1]
        arr['frequency'][min_index] = new_value
        arr['end'][min_index] = arr['end'][min_index + 1]
        del arr['start'][min_index + 1]
        del arr['end'][min_index + 1]
        del arr['frequency'][min_index + 1]

    return arr

#Разбить на заданное количество интервалов
def split(arr, maxIntervals, minFrequency = 5):
    intervals = split_array_into_intervals(arr, minFrequency)
    if len(intervals['start']) < maxIntervals:
        raise ValueError("Невозможно разбить на заданное количество интервалов")
    while len(intervals['start']) > maxIntervals:
        intervals = min_sum(intervals)
    return intervals

