#przykladowy program 2
#Mnozenie i sortowanie macierzy
import numpy as np
import time


class Array_Multiplicator(object):
    def __init__(self, size_of_vector):
        self.vector_size = size_of_vector
        self.random_numbers_one = np.random.rand(self.vector_size, self.vector_size)
        self.random_numbers_two = np.random.rand(self.vector_size, self.vector_size)
        self.random_numbers_three = 0
        self.random_numbers_four = 0
        self.random_numbers_five = 0
        self.random_numbers_six = 0
        self.initial_time = 0
        self.ending_time = 0
        self.execution_time = 0

    def multiply_array(self):
        self.initial_time = time.time()
        self.random_numbers_three = np.dot(self.random_numbers_one, self.random_numbers_two)
        self.random_numbers_four = np.dot(self.random_numbers_two, self.random_numbers_three)
        self.random_numbers_five = np.dot(self.random_numbers_three, self.random_numbers_four)
        self.random_numbers_six = np.dot(self.random_numbers_four, self.random_numbers_five)
        self.ending_time = time.time()
        self.execution_time += self.ending_time - self.initial_time
        print("Execution time after multiplying is:", self.execution_time)

    def sort_array(self):
        self.initial_time = time.time()
        np.sort(self.random_numbers_one)
        np.sort(self.random_numbers_two)
        np.sort(self.random_numbers_three)
        np.sort(self.random_numbers_four)
        np.sort(self.random_numbers_five)
        np.sort(self.random_numbers_six)
        self.ending_time = time.time()
        self.execution_time += self.ending_time - self.initial_time
        print("Execution time of all array operations is:", self.execution_time)


array_Operations = Array_Multiplicator(1000)
array_Operations.multiply_array()
array_Operations.sort_array()