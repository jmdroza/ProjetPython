from imp import get_tag
from unittest import TestCase

from meteo import hexa_to_temperature, get_full_tag


class Test(TestCase):
    def test_hexa_to_temperature(self):
        assert hexa_to_temperature("40D4") == -22.7
        assert hexa_to_temperature("00E3") == 22.7
        assert hexa_to_temperature("001A") == 2.6
        assert hexa_to_temperature("007F") == 12.7
        assert hexa_to_temperature("00E3") == 22.7
        assert hexa_to_temperature("00FF") == 25.5
        assert hexa_to_temperature("0154") == 34.0
        assert hexa_to_temperature("0191") == 40.1


class Test(TestCase):
    def test_hexa_to_date(self):
        assert hexa_to_temperature("120C0D021D11") == "2018/12/13 02:29:17"


class Test(TestCase):
    def test_get_full_tag(self):
        data = "545A003624240406020000000641884907900001120C0D021D1100000008AAC00000019F04D0000E00010B62180983000E3300D42D2D005129D30D0A"
        assert get_full_tag(data) == "000E00010B62180983000E3300D42D2D"
