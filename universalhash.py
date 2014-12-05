#in universal hashing, a random function from a family of hash functions is chosen

#let p = max of possible keys and also prime
#let a is a random number from 0 to 1, and b is any number between o and p-1
#hashf(a,b))(k) = ((ak+b)%p)%m) where m is length of hash table

import sys, random

class UniversalHash:

	def __init__(self, size):
		self.size = int(size)
		self.hashtable = (None,)*self.size
		self.p = self._get_prime()
		self.a = random.random()
		self.b = random.randint(0, self.p-1)

	def _isprime(self, n):
		if n <= 2 or n%2 == 0:
			return False
		return not any((n%i==0 for i in range(3,n-1)))

	def _get_prime(self):
		p = random.randint(1000000,10000000)
		while not self._isprime(p):
			p+=1
		return p

	def hash_func(self, hashkey):
		print("Hash Function parameters: P is %s, A is %s, B is %s"%(self.p, self.a, self.b))
		return ((self.a*hashkey + self.b)%self.p)%self.size

	def probing_hash(self, hashkey):
		print("Probing")
		probe_hash = 1 + hashkey%(self.size -1)
		while not self._isprime(probe_hash):
			probe_hash+=1
		return probe_hash%self.size

	TROUBLESHOOTING HASH TABLE!
	SOME RECURSION ERRORS

	# def __getattr__(self, key):
	# 	i=0
	# 	hashval = self.hash_func(key) + i*self.probing_hash(key)
	# 	if self.hashtable[hashval][0] == None:
	# 		raise KeyError("Key does not exist")
	# 	while self.hashtable[hashval][0] != key:
	# 		i+=1
	# 		hashval = self.hash_func(key) + i*self.probing_hash(key)
	# 	return self.hashtable[hashval]


	# def __setattr__(self, key, value):
	# 	i=0
	# 	hashval = self.hash_func(key) + i*self.probing_hash(key)
	# 	while self.hashtable[hashval][0] != None or self.hashtable[hashval][0] != "DEL":
	# 		i+=1
	# 		hashval = self.hash_func(key) + i*self.probing_hash(key)
	# 	self.hashtable[hashval] = (key, value)	


if __name__ == '__main__':
#arguments should be the size of the hash table
	hash_size = sys.argv[1]
	print("Hash table size will be %s"%hash_size)

	test_table = UniversalHash(hash_size)


	


#generate p
#table size 1000