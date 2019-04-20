import unittest
from mc_funnist import *


class MyFirstTests(unittest.TestCase):
	def test_joke(self):
		self.assertEqual(joke(), u'This is my first python package!')


if __name__ == '__main__':
	unittest.main()