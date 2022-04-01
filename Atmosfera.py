import numpy
class Atmosphere:
    def __init__(self, height):
        self.height = height
        # self.in_troposphere = False
        # self.in_stratosphere = False

    def __repr__(self):
        return f'<Atmosphere parameters for height . >'

    def __str__(self):
        return f'Returns atmosphere parameters for height {self.height} ' \
               f'Input height should be in  [m]. ' \
               f'Output temperature is in [K]' \
               f'Output pressure is in [Pa]' \
               f'Output density is in [kg/m^3]'

    """def atmosphere_layer(self):
        if self.height <= 11000.0:
            self.in_troposphere = True
            print("Troposphere model will be used")
        elif self.height > 11000.0:
            self.in_stratosphere = True
            print("Stratosphere model will be used")
            """

    def temperature(self):
        # Temperature return is in [K]
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


troposphere_test = Atmosphere(0)
troposphere_temperature = troposphere_test.temperature()
troposphere_density_troposphere = troposphere_test.density()
troposphere_pressure = troposphere_test.pressure()
troposphere_dynamic_viscosity = troposphere_test.dynamic_viscosity()
troposphere_kinematic_viscosity = troposphere_test.kinematic_viscosity()
troposphere_sound_speed = troposphere_test.sound_speed()

stratosphere_test = Atmosphere(50000)
startosphere_temperature = stratosphere_test.temperature()
startosphere_density = stratosphere_test.density()
startosphere_pressure = stratosphere_test.pressure()

# Troposfera
"""
T0 = 288.15  # K
p0 = 1013.25  # hpa
rho0 = 1.225  # kg/m^3
a0 = 340.3  # m/s
mi0 = 1.40607 * 10 ** (-5)  # m^2/s
# stratosfera (do 20 km) T = const
Tstrat = 216.5  # K
"""