import unittest

class Test1(unittest.TestCase):
	def setUp(self):
		print "---start test"

	def tearDown(self):
		print "----end test"

	def test_firsttest(self):
		self.assertEqual(1, 1) 

suite = unittest.TestLoader().loadTestsFromTestCase(Test1)
unittest.TextTestRunner(verbosity=2).run(suite)