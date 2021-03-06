"""
Created at 18.03.2020

@author: Piotr Bartman
@author: Sylwester Arabas
"""

from . import conf
import numba
from numba import boolean, int64


class Methods:

    @staticmethod
    def apply(function, args, output):
        if len(args) == 3:
            if len(output) == 3:
                Methods._apply_f_3_3(function, *args, *output)
            else:
                raise NotImplementedError()
        else:
            raise NotImplementedError()

    @staticmethod
    @numba.njit(boolean(int64[:]), **{**conf.JIT_FLAGS, **{'parallel': False}})
    def first_element_is_zero(array):
        return array[0] == 0

    @staticmethod
    @numba.njit(**{**conf.JIT_FLAGS, **{'parallel': False, 'cache': False}})
    def _apply_f_3_3(function, arg0, arg1, arg2, output0, output1, output2):
        for i in range(output0.shape[0]):
            output0[i], output1[i], output2[i] = function(arg0[i], arg1[i], arg2[i])