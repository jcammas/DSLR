import argparse
import math
import numpy as np


def count(data):
    count = 0
    for i in data:
        if not np.isnan(i):
            count += 1
    return float(count)


def mean(data):
    """
    mean() function can be used to calculate mean/average of a given list of numbers. 
    It returns mean of the data set passed as parameters. 
    Arithmetic mean is the sum of data divided by the number of data-points
    """
    sum = 0
    c = count(data)
    for i in data:
        if not np.isnan(i):
            sum += i
    mean = sum / c
    return float(mean)

# Pour deux ensembles de données ayant la même moyenne,
# celui dont l'écart-type est le plus grand est celui dans lequel les données sont les plus dispersées par rapport au centre.
# L'écart-type est égal à 0 zéro si toutes les valeurs d'un ensemble de données sont les mêmes (parce que chaque valeur est égale à la moyenne).


def std(data):
    """
    Standard deviation is a number that describes how spread out the values are. 
    A low standard deviation means that most of the numbers are close to the mean (average) value. 
    A high standard deviation means that the values are spread out over a wider range
    """
    m = mean(data)
    c = count(data)
    sum_std = 0
    for i in data:
        if not np.isnan(i):
            sum_std += (i - m) ** 2
    var = sum_std / c
    std = var ** (0.5)
    return float(std)


def percentile_(data, perc: int):
    size = len(data)
    idx = int(math.ceil((size * perc) / 100)) - 1
    return sorted(data)[idx]


def quartile_low(x):
    if len(x) == 0:
        return None

    q1 = percentile_(x, 25)

    return [q1]


def quartile_med(x):
    if len(x) == 0:
        return None

    q2 = percentile_(x, 50)

    return [q2]


def quartile_high(x):
    if len(x) == 0:
        return None

    q3 = percentile_(x, 75)

    return [q3]


def min(x):
    min_ = x[0]
    for i in x:
        val = i
        if val < min_:
            min_ = val
    return min_


def max(x):
    max_ = x[0]
    for i in x:
        val = i
        if val > max_:
            max_ = val
    return max_


def unique(data):
    """
    The unique() function is used to find the unique elements of an array. 
    Returns the sorted unique elements of an array. 
    There are three optional outputs in addition to the unique elements: the indices of the input array that give the unique values. 
    the indices of the unique array that reconstruct the input array.
    """
    unique = []
    for i in data:
        if not np.isnan(i) and i not in unique:
            unique.append(i)
    return len(unique)


def freq(data):
    freq = []
    numbers = []
    for i in data:
        if not np.isnan(i) and i not in freq:
            freq.append(i)
            numbers.append(1)
        elif not np.isnan(i):
            numbers[freq.index(i)] += 1
    return numbers[numbers.index(max(numbers))]
