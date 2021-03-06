"""
Created at 05.02.2020

@author: Piotr Bartman
@author: Sylwester Arabas
"""

from PySDM.product import MomentProduct
from PySDM.physics import constants as const


class TotalParticleSpecificConcentration(MomentProduct):
    def __init__(self, particles_builder):

        super().__init__(
            particles=particles_builder.particles,
            shape=particles_builder.particles.mesh.grid,
            name='n_mg',
            unit='mg-1',
            description='Total particle specific concentration',
            scale='linear',
            range=[20, 50]
        )

    def get(self):
        self.download_moment_to_buffer('volume', rank=0)
        result = self.buffer.copy()  # TODO !!!
        self.download_to_buffer(self.particles.environment['rhod'])
        result[:] /= self.particles.mesh.dv
        result[:] /= self.buffer
        const.convert_to(result, const.si.milligram**-1)
        return result
