import unittest
from controllers import Multilevel_Inheritance

class TestMultilevelInheritance(unittest.TestCase):

    def test_getName(self):
    	# Asume its true
    	res = Multilevel_Inheritance.GrandChild('Ken Dan', 18, 'Cebu City')

    	# Assert
    	self.assertTrue(res.getName(), "Ken Dan")

    def test_getAge(self):
    	# Asume its true
    	res = Multilevel_Inheritance.GrandChild('Ken Dan', 18, 'Cebu City')

    	# Assert
    	self.assertTrue(res.getAge(), 18)

    def test_getAddress(self):
    	# Asume its true
    	res = Multilevel_Inheritance.GrandChild('Ken Dan', 18, 'Cebu City')

    	# Assert
    	self.assertTrue(res.getAddress(), 'Cebu City')
