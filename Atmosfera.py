import numpy


class Atmosphere:
    def __init__(self, height):
        self.height = height

    def __repr__(self):
        return f'<Atmosphere parameters for input height . >'

    def __str__(self):
        return f'Returns atmosphere parameters for height {self.height} ' \
               f'Input height should be in  [m]. ' \
               f'Output temperature is in [K]' \
               f'Output pressure is in [Pa]' \
               f'Output density is in [kg/m^3]'

    def temperature(self):
        if self.height < 11000.0:
            return 288.15 - self.height / 1000 * 6.5
        else:
            return 216.5

    def density(self):
        if self.height < 11000.0:
            return 1.255 * (1 - self.height / 44330) ** 4.256
        else:
            return 0.3639 * numpy.exp((self.height - 11000) / 6340)

    def pressure(self):
        if self.height < 11000.0:
            return 101325 * (1 - self.height / 44300) ** 5.256
        else:
            return 22632 * numpy.exp((self.height - 11000) / 6340)

    def sound_speed(self):
        return 340.3 * numpy.sqrt(self.temperature() / 288.15)

    def dynamic_viscosity(self):
        return 1.458 * 10 ** (-6) * self.temperature() ** 1.5 / (self.temperature() + 100.4)

    def kinematic_viscosity(self):
        return 1.40607 * 10 ** (-5) * 101325 / self.pressure() * (self.temperature() / 288.15) ** 1.754
