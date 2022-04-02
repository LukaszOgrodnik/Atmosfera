from unittest import result
from Atmosfera import Atmosphere 
#poprawić tę składnię
Test_atm = Atmosphere(0)

class TestAtmosfera:
    def test_density(self):
        result= Test_atm.density
        assert  result(1.225)