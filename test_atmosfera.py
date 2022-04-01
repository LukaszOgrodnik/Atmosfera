from unittest.mock import patch
import pytest

from Atmosfera import Atmosphere


@pytest.fixture
def sea_level_temp():
    return 288.15


class TestAtmosfera:

    def test_temperature(self, sea_level_temp):
        atm = Atmosphere(0)
        result = atm.temperature()

        assert result == sea_level_temp

    @patch('Atmosfera.Atmosphere.temperature')
    def test_sound_speed(self, mock_temperature):
        atm = Atmosphere(0)
        mock_temperature.return_value = 288.15
        result = atm.sound_speed()

        assert result == 340.3