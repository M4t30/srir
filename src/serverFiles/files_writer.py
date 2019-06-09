#przykladowy program 3
#Zapis do pliku
import numpy as np
import time


class Writer_To_File(object):
    def __init__(self, size_of_vector, filename):
        self.vector_size = size_of_vector
        self.file = 0
        self.filename = filename
        self.random_numbers = np.random.rand(self.vector_size)
        self.initial_time = 0
        self.ending_time = 0
        self.execution_time = 0

    def write_to_file(self):
        try:
            self.file = open(self.filename, 'w+')
            self.initial_time = time.time()
            for item in self.random_numbers:
                self.file.write("%s\n" % item)
            self.ending_time = time.time()
            self.file.close()
        except Exception as e:
            print(e)

        self.execution_time = self.ending_time - self.initial_time
        print("Execution time is:", self.execution_time)


files_Operations = Writer_To_File(1000000, "plik.txt")
files_Operations.write_to_file()
