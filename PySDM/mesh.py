"""
Created at 28.11.2019

@author: Piotr Bartman
@author: Sylwester Arabas
"""

import numpy as np
from PySDM.backends.numba.numba import Numba


class Mesh:

    def __init__(self, grid, size):
        self.grid = grid
        self.size = size
        self.strides = Mesh.__strides(grid)
        self.n_cell = int(np.prod(grid))
        self.dv = np.prod((np.array(size) / np.array(grid)))
        self.__dimension = len(self.grid)

    @property
    def dz(self):
        return self.size[-1] / self.grid[-1]

    @property
    def dimension(self):
        return self.__dimension

    @property
    def dim(self):
        return self.dimension

    @staticmethod
    def mesh_0d(dv=None):
        mesh = Mesh((1,), ())
        mesh.dv = dv
        mesh.__dimension = 0
        return mesh

    @staticmethod
    def __strides(grid):
        domain = np.empty(tuple(grid))  # TODO optimize
        strides = np.array(domain.strides).reshape(1, -1) // domain.itemsize
        return strides

    def cellular_attributes(self, positions):
        n = positions.shape[1]
        cell_origin = positions.astype(dtype=np.int64)
        position_in_cell = positions - np.floor(positions)

        cell_id = np.empty(n, dtype=np.int64)
        Numba.cell_id(cell_id, cell_origin, self.strides)

        return cell_id, cell_origin, position_in_cell
