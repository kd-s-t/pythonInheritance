import unittest
from controllers import Inheritance

class TestInheritance(unittest.TestCase):

    def test_chest(self):
    	# Asume its true
    	body = Inheritance.Body()

    	# Action
    	chest = body.chest()

    	# Assert
    	self.assertTrue(chest, "I have chest")

    def test_stomach(self):
    	# Asume its true
    	body = Inheritance.Body()

    	# Action
    	stomach = body.stomach()

    	# Assert
    	self.assertTrue(stomach, "I have stomach")

    def test_eyes(self):
    	# Asume its true
    	body = Inheritance.Body()

    	# Action
    	eyes = body.eyes()

    	# Assert
    	self.assertTrue(eyes, "I have eyes")

    def test_ears(self):
    	# Asume its true
    	body = Inheritance.Body()

    	# Action
    	ears = body.ears()

    	# Assert
    	self.assertTrue(ears, "I have ears")
