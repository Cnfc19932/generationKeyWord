import unittest
import main as m
#import sys


class removeBadChar(unittest.TestCase):
	def setUp(self):
		#print sys.path
#		a =  
		pass

	def tearDown(self):
	#	print "----end test"
		pass
	def test_firsttest(self):
		#pass
		k = m.WordProperties()._remove_bad_char('23')
		self.assertEqual([u'23'], k) 

suite = unittest.TestLoader().loadTestsFromTestCase(removeBadChar)
unittest.TextTestRunner(verbosity=2).run(suite)