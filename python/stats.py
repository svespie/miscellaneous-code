# this is just an exercise in programming, nothing fancy - most of the logic is already implemented in standard python
# it is assumed that set is a row vector (1D array) composed of numbers
# warning - no error handling is implemented

import random
import math
import argparse

from enum import Enum

import sort

class StandardDeviationMethod(Enum):
    POPULATION = 1      # full set
    SAMPLE = 2          # sample set

class SimpleStats():
    def __init__(self):
        pass

    def compute_minimum(self, set):
        # could sort and then take the first item but we can iterate just once
        if len(set) == 0:
            return None
        if len(set) == 1:
            return set[0]
        min_value = set[0]
        for i in range(1,len(set)):
            if set[i] < min_value:
                min_value = set[i]
        return min_value
    
    def compute_maximum(self, set):
        # could sort and then take the first item but we can iterate just once
        if len(set) == 0:
            return None
        if len(set) == 1:
            return set[0]
        max_value = set[0]
        for i in range(1, len(set)):
            if set[i] > max_value:
                max_value = set[i]
        return max_value
    
    def compute_range(self, set):
        min_val = self.compute_minimum(set)
        max_val = self.compute_maximum(set)
        if min_val == None or max_val == None:
            return None
        if min_val == max_val:
            return min_val
        return max_val - min_val
    
    def compute_sum(self, set):
        sum = 0
        for item in set:
            sum += item
        return sum
    
    def compute_mean(self, set):
        sum = self.compute_sum(set)
        return sum / len(set)

    def compute_median(self, set):
        if len(set) == 0:
            return None
        if len(set) == 1:
            return set[0]
        s = sort.selection_sort_ascending(set.copy())
        while len(s) > 2:
            s = s[1:-1]
        if len(s) == 2:
            return (s[0] + s[1]) / 2
        return s[0]

    def compute_mode(self, set):
        if len(set) == 0:
            return [], None
        frequency_counters = {}
        for item in set:
            frequency_counters.setdefault(item, 0)
            frequency_counters[item] += 1
        max_frequency = max(frequency_counters.values())
        modes = []
        for number, frequency in frequency_counters.items():
            if frequency == max_frequency:
                modes.append(number)
        return modes, max_frequency

    def compute_variance(self, set, method = StandardDeviationMethod.SAMPLE):
        # population => sum((i-x)^2)/n; where i is a given value in the set, x is the mean of the set, n is number of items in the set
        # sample => sum((i-x)^2)/n-1; where i is a given value in the set, x is the mean of the set, n is number of items in the set
        mean = self.compute_mean(set)
        deviation_square_sum = 0
        for item in set:
            deviation = item - mean
            deviation_square_sum += deviation ** 2
        denominator = len(set)
        if method == StandardDeviationMethod.SAMPLE:
            denominator = denominator - 1
        return deviation_square_sum / denominator

    def compute_standard_deviation(self, set, method = StandardDeviationMethod.SAMPLE):
        variance = self.compute_variance(set, method)
        return math.sqrt(variance)

if __name__ == "__main__":
    DEFAULT_SET_SIZE = 20
    DEFAULT_MAGNITUDE = 5

    def generate_random_set(size = DEFAULT_SET_SIZE, magnitude = DEFAULT_MAGNITUDE):
        # taking a simplistic approach
        set = []
        while len(set) < size:
            set.append(random.randint(-magnitude, magnitude))
        return set
    
    parser = argparse.ArgumentParser(description="Demo script displaying simple stats of a row vector data set")
    parser.add_argument("-s","--size",required=False,default=DEFAULT_SET_SIZE,action="store",help=f"the size of the dataset to create (default: {DEFAULT_SET_SIZE})")
    parser.add_argument("-m","--magnitude",required=False,default=DEFAULT_MAGNITUDE,action="store",help=f"distance from 0 that values should range (default: {DEFAULT_MAGNITUDE})")
    args = parser.parse_args()
    set_size = int(args.size)
    set_magnitude = int(args.magnitude)
    stats = SimpleStats()
    #set = [1,3,5,7,9,2,4,6,8]
    set = generate_random_set(set_size, set_magnitude)
    sorted_set = sort.selection_sort_ascending(set)
    min_value = stats.compute_minimum(set)
    max_value = stats.compute_maximum(set)
    set_range = stats.compute_range(set)
    sum = stats.compute_sum(set)
    mean = stats.compute_mean(set)
    median = stats.compute_median(set)
    modes, frequency = stats.compute_mode(set)
    std_dev_method = StandardDeviationMethod.SAMPLE
    variance = stats.compute_variance(set, std_dev_method)
    std_dev = stats.compute_standard_deviation(set, std_dev_method)

    print(f"set:      {set}")
    print(f"sorted:   {sorted_set}")
    print(f"min:      {min_value}")
    print(f"max:      {max_value}")
    print(f"range:    {set_range}")
    print(f"sum:      {sum}")
    print(f"mean:     {mean}")
    print(f"median:   {median}")
    print(f"mode{'(s):' if len(modes)>1 else ':   '}  {modes if modes else 'none'} {'(frequency = '+str(frequency)+')' if frequency else ''}")
    print(f"variance: {variance} (method = {std_dev_method.name})")
    print(f"std dev:  {std_dev} (method = {std_dev_method.name})")