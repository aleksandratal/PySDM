"""
Created at 05.02.2020

@author: Piotr Bartman
@author: Sylwester Arabas
"""

from ...product import Product
from PySDM.environments._moist import _Moist


class RelativeHumidity(Product):
    def __init__(self, particles_builder):
        particles = particles_builder.particles
        assert isinstance(particles.environment, _Moist)
        self.environment = particles.environment
        super().__init__(particles=particles,
                         description="Relative humidity",
                         name="RH",
                         unit="%",
                         range=(75, 105),
                         scale="linear",
                         shape=particles.mesh.grid)

    def get(self):
        self.download_to_buffer(self.environment['RH'])
        self.buffer *= 100
        return self.buffer
