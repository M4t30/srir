#przykladowy program 1
#Suma wszystkich elementow listy
import numpy as np
import time


class Array_Summator(object):
    def __init__(self, size_of_vector):
        self.vector_size = size_of_vector
        self.random_numbers = np.random.rand(self.vector_size)
        self.sum = 0
        self.initial_time = 0
        self.ending_time = 0
        self.execution_time = 0

    def sum_array(self):
        self.initial_time = time.time()
        self.sum = np.sum(self.random_numbers)
        self.ending_time = time.time()
        self.execution_time = self.ending_time - self.initial_time
        print("The sum is:", self.sum)
        print("Execution time is:", self.execution_time)


summator = Array_Summator(100000000)
summator.sum_array()