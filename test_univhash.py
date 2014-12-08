#Test Universal Hash Table

import unittest, pdb 
from universalhash import UniversalHash

class Test_Hash(unittest.TestCase):

	def setUp(self):
		self.test_table = UniversalHash(100)

	def test_get_prime(self):
		next_prime = self.test_table._get_prime(42)
		next_prime2 = self.test_table._get_prime(502)
		self.assertEqual(next_prime, 43)
		self.assertEqual(next_prime2, 503)

	def test_hashfunc(self):
		self.test_table.p = 119
		self.test_table.a = .6667
		self.test_table.b = 11
		testhash = 21
		test_value = ((round(self.test_table.a*testhash+self.test_table.b))%self.test_table.p)%self.test_table.size
		hash_val = self.test_table.hash_func(testhash)
		self.assertEqual(test_value, hash_val)

	def test_getitem(self):
		self.test_table = UniversalHash(1000)
		with self.assertRaises(KeyError):
			self.test_table[19]
		self.test_table[26] = "James"
		self.assertEqual(self.test_table[26], "James")

	def test_deleteitem(self):
		self.test_table = UniversalHash(10)
		self.test_table[300] = "Laura"
		self.test_table[2201] = "Ted"
		self.test_table[26] = "Jillian"
		self.test_table.delete_item(26)
		hashv = self.test_table.hash_func(26)%10
		self.assertEqual(self.test_table.hashtable[hashv][0], "DEL")
		

	def test_len(self):
		self.test_table = UniversalHash(10)
		self.test_table[300] = "Laura"
		self.test_table[2201] = "Ted"
		self.test_table[26] = "Jillian"
		self.assertEqual(self.test_table.length, 3)

	def test_keys_vals(self):
		self.test_table = UniversalHash(10)
		self.test_table[300] = "Laura"
		self.test_table[2201] = "Ted"
		self.test_table[26] = "Jillian"
		self.assertIn(300, self.test_table.keys)
		self.assertIn(2201, self.test_table.keys)
		self.assertIn(26, self.test_table.keys)
		self.assertIn("Laura", self.test_table.values)
		self.assertIn("Ted", self.test_table.values)
		self.assertIn("Jillian", self.test_table.values)



if __name__ =='__main__':
	unittest.main()


