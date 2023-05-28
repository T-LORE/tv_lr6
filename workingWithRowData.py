import numpy as np
from graphingFunctions import roundValue
from scipy import integrate
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
def split(arr, maxIntervals):
    arr = np.sort(arr)
    
    diff = (arr[-1] - arr[0]) / maxIntervals
    
    intervals = {
        'start' : [],
        'end' : [],
        'frequency' : []
    }
    
    for i in range(maxIntervals):
        intervals['start'].append(arr[0] + diff * i)
        intervals['end'].append(arr[0] + diff * (i + 1))
        intervals['frequency'].append(0)
        
    for i in range(len(arr)):
        for j in range(len(intervals['start'])):
            if (arr[i] > intervals['start'][j] and arr[i] <= intervals['end'][j]) or (j == 0 and arr[i] == intervals['start'][j]):
                intervals['frequency'][j] += 1
                break
    print(intervals)
    return intervals    
    
    # intervals = split_array_into_intervals(arr, minFrequency)
    # if len(intervals['start']) < maxIntervals:
    #     raise ValueError("Невозможно разбить на заданное количество интервалов")
    # while len(intervals['start']) > maxIntervals:
    #     intervals = min_sum(intervals)
    # return intervals

    
def simpsonRule(func, start, end, n):
    h = (end - start) / (2 * n)
    x = [start + i * h for i in range(2 * n + 1)]
    y = [func(x[i]) for i in range(2 * n + 1)]
    integral = (end - start) / (6 * n) * sum([y[i-1] + 4 * y[i] + y[i+1] for i in range(1, 2*n, 2)])
    return integral

# теоретическиtе вероятности рi попадания значений предполагаемой нормально распределенной случайной величины в соответствующие интервалы значений X
def getPi(aStar, sigmaStar, intervals):
    underIntegral = lambda x: np.exp(-(x ** 2) /2)
    pi = []
    coef = 1 / (np.sqrt(2 * np.pi))
    for i in range(len(intervals['start'])):
        startIntegral = (intervals['start'][i]- aStar) / sigmaStar
        endIntegral = (intervals['end'][i] - aStar) / sigmaStar   
        pi.append(roundValue(coef * simpsonRule(underIntegral, startIntegral, endIntegral, 5)))
    return pi

def libGetPi(aStar, sigmaStar, intervals):
    underIntegral = lambda t: np.exp(-(t ** 2) /2)
    pi = []
    coef = 1 / (np.sqrt(2 * np.pi))
    for i in range(len(intervals['start'])):
        u1 = (intervals['start'][i]- aStar) / sigmaStar
        u2  = (intervals['end'][i] - aStar) / sigmaStar
        Fu1 = coef * integrate.fixed_quad(underIntegral, 0, u1, n = 2)[0]
        Fu2 = coef * integrate.fixed_quad(underIntegral, 0, u2, n = 2)[0]
        pi.append(round(Fu2 - Fu1, 5))
    return pi
    
   
def gethi2ObservedArray(frequency, p):
    hi2Observed = []
    for i in range(len(p)):
        hi2Observed.append(((frequency[i] - p[i] * sum(frequency)) ** 2) / (p[i] * sum(frequency)))
    return hi2Observed

