import unittest
from controllers import Multiple_Inheritance

class TestMultipleInheritance(unittest.TestCase):

    def test_id(self):
    	# Asume its true
    	res = Multiple_Inheritance.Resident('Ken Dan', 18, '10305504')

    	# Assert
    	self.assertTrue(res.getId(), "10305504")

    def test_showName(self):
    	# Asume its true
    	res = Multiple_Inheritance.Resident('Ken Dan', 18, '10305504')

    	# Assert
    	self.assertTrue(res.showName(), "Ken Dan")

    def test_showAge(self):
    	# Asume its true
    	res = Multiple_Inheritance.Resident('Ken Dan', 18, '10305504')

    	# Assert
    	self.assertTrue(res.showAge(), 18)
