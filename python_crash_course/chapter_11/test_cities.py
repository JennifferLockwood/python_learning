import unittest
from city_functions import city_country


class CitiesTestCase(unittest.TestCase):
    """Test for 'city_functions.py', as part of TIY 11-1."""

    def test_city_country(self):
        """Do pairs like 'Santiago, Chile' work?"""
        formatted_city_country = city_country('santiago', 'chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do values like 'Santiago, Chile - population 5000000' work?"""
        formatted_city_country = city_country('santiago', 'chile', '5000000')
        self.assertEqual(formatted_city_country, 'Santiago, Chile - population 5000000')

unittest.main()
