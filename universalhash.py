#in universal hashing, a random function from a family of hash functions is chosen

#let p = max of possible keys and also prime
#let a is a random number from 0 to 1, and b is any number between o and p-1
#hashf(a,b))(k) = ((ak+b)%p)%m) where m is length of hash table

import sys, random, pdb

class UniversalHash:

	def __init__(self, size):
		self.size = int(size)
		self.hashtable = tuple([[None, None] for x in range(self.size)])
		self.p = self._get_prime()
		self.a = random.random()
		self.b = random.randint(0, self.p-1)

	def _isprime(self, n):
		if n <= 2 or n%2 == 0:
			return False
		return not any((n%i==0 for i in range(3,n-1)))

	def _get_prime(self, p=0):
		if p ==0:
			p = random.randint(1000000,10000000)
		while not self._isprime(p):
			p+=1
		return p

	def hash_func(self, hashkey):
		return ((round(self.a*hashkey + self.b))%self.p)%self.size

	def probing_hash(self, hashkey):
		probe_hash = 1 + hashkey%(self.size -1)
		while not self._isprime(probe_hash):
			probe_hash+=1
		return probe_hash%self.size

	def __getitem__(self, key):
		i=0
		hashval = (self.hash_func(key) + i*self.probing_hash(key))%self.size 
		if self.hashtable[hashval][0] == None:
			raise KeyError("Key does not exist")
		while self.hashtable[hashval][0] != key and i < self.size:
			i+=1
			hashval = (self.hash_func(key) + i*self.probing_hash(key))%self.size 
		if i < self.size:
			return self.hashtable[hashval][1]
		else:
			raise RuntimeError("Unable to find item")


	def __setitem__(self, key, value):
		i=0
		hashval = (self.hash_func(key) + i*self.probing_hash(key))%self.size 
		while self.hashtable[hashval][0] != None and i < self.size:
			i+=1
			hashval = (self.hash_func(key) + i*self.probing_hash(key))%self.size 
		if i < self.size:
			self.hashtable[hashval][0] = key
			self.hashtable[hashval][1] = value
		else:
			raise RuntimeError("Unable to set item")

	def delete_item(self, key):
		i=0
		hashval = (self.hash_func(key) + i*self.probing_hash(key))%self.size 
		while self.hashtable[hashval][0] != key and i < self.size:
			i+=1
			hashval = (self.hash_func(key) + i*self.probing_hash(key))%self.size 
		if i < self.size:
			self.hashtable[hashval][1] = None
			self.hashtable[hashval][0] = "DEL"	
		else:
			raise RuntimeError("Unable to delete item")



if __name__ == '__main__':
#arguments should be the size of the hash table
	hash_size = sys.argv[1]
	print("Hash table size will be %s"%hash_size)

	test_table = UniversalHash(hash_size)


	


#generate p
#table size 1000