from unittest.mock import patch
import pytest

from atmosfera.atmosfera import Atmosphere


@pytest.fixture
def sea_level_temp():
    return 288.15

@pytest.fixture
def sea_level_density():
    return 1.255

@pytest.fixture
def sea_level_pressure():
    return 101325.0


class TestAtmosfera:

    def test_temperature(self, sea_level_temp):
        atm = Atmosphere(0)
        result = atm.temperature()

        assert result == sea_level_temp

    def test_temperature_stratosphere(self):
        atm = Atmosphere(11000)
        result = atm.temperature()

        assert result == 216.5

    def test_density(self, sea_level_density):
        atm = Atmosphere(0)
        result = atm.density()

        assert result == sea_level_density

    def test_pressure(self, sea_level_pressure):
        atm = Atmosphere(0)
        result = atm.pressure()

        assert result == sea_level_pressure


    @patch('atmosfera.atmosfera.Atmosphere.temperature')
    def test_sound_speed(self, mock_temperature):
        atm = Atmosphere(0)
        mock_temperature.return_value = 288.15
        result = atm.sound_speed()

        assert result == 340.3

    # @patch('atmosfera.atmosfera.Atmosphere.temperature')
    # def test_dynamic_viscosity(self, mock_temperature):
    #     atm = Atmosphere(0)
    #     mock_temperature.return_value = 288.15
    #     result = atm.dynamic_viscosity()
    #
    #     assert result == 1.458 * 10 ** (-6)