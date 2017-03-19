import unittest
import rpn
class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('2 2 ^')
		self.assertEqual(4, result)
	def test_subtract(self):
		result = rpn.calculate('5 2 ^')
		self.assertEqual(25, result)