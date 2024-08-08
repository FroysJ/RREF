from libcpp.vector cimport vector
from libcpp.utility cimport pair

cdef extern from "Solution.h":
    cdef cppclass Solution:
        @staticmethod
        vector[vector[int]] int_rref(vector[vector[int]]& matrix)
        @staticmethod
        vector[int] int_sdiv(vector[int]& p, vector[int]& d)

# Python class to wrap the Solution class
cdef class PySolution:
    cdef Solution* thisptr

    def __cinit__(self):
        # Solution is a static class, so no instance is needed
        pass

    def int_rref(self, matrix):
        return Solution.int_rref(matrix)

    def int_sdiv(self, p, d):
        return Solution.int_sdiv(p, d)
