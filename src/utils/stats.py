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
    sum = 0
    c = count(data)
    for i in data:
        if not np.isnan(i):
            sum += i
    mean = sum / c
    return float(mean)


def std(data):
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
