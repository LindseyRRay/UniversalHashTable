#in universal hashing, a random function from a family of hash functions is chosen

#let p = max of possible keys and also prime
#let a is a random number from 0 to 1, and b is any number between o and p-1
#hashf(a,b))(k) = ((ak+b)%p)%m) where m is length of hash table

import sys, random, pdb

def _isprime(n):
		if n <= 2 or n%2 == 0:
			return False
		return not any((n%i==0 for i in range(3,n-1)))

def hash_func(hashkey, size, a, b, p):
	return ((round(a*hashkey + b))%p)%size

def probing_hash(hashkey, size):
	probe_hash = 1 + hashkey%(size -1)
	while not _isprime(probe_hash):
		probe_hash+=1
	return probe_hash%size

def linear_probing():
	return 1

def quadratic_probing(hashkey, size):
	return ((hashkey^2)%(size -1))

# Solely for use in the timeit module
funcs = [probing_hash, linear_probing, quadratic_probing]

class UniversalHash:

	def __init__(self, size, hash_func=hash_func, probing_hash = probing_hash):
		self.size = int(size)
		self.hashtable = tuple([[None, None] for x in range(self.size)])
		self.collisions = [0 for x in range(self.size)]
		self.p = self._get_prime()
		self.a = random.random()
		self.b = random.randint(0, self.p-1)
		self.hash_func = hash_func
		self.probing_hash = probing_hash
		self.unable_to_set = 0

	def _isprime(self, n):
		if n <= 2 or n%2 == 0:
			return False
		return not any((n%i==0 for i in range(3,n-1)))

	def _get_prime(self, p=0):
		if p == 0:
			p = random.randint(1000000,10000000)
		while not self._isprime(p):
			p+=1
		return p

	def __getitem__(self, key):
		i=0
		hashval = (hash_func(key, self.size, self.a, self.b, self.p) + i*probing_hash(key, self.size))%self.size 
		if self.hashtable[hashval][0] == None:
			raise KeyError("Key does not exist")
		while self.hashtable[hashval][0] != key and i < self.size:
			i+=1
			hashval = (hash_func(key, self.size, self.a, self.b, self.p) + i*probing_hash(key, self.size))%self.size 
		if i < self.size:
			return self.hashtable[hashval][1]
		else:
			raise RuntimeError("Unable to find item")


	def __setitem__(self, key, value):
		i=0
		hashval = (hash_func(key, self.size, self.a, self.b, self.p) + i*probing_hash(key, self.size))%self.size  
		while self.hashtable[hashval][0] != None and i < 100*self.size:
			i+=1
			print("Iteration %s and key is %s and hashval is %s"%(i, key, hashval))
			hashval = (hash_func(key, self.size, self.a, self.b, self.p) + i*probing_hash(key, self.size))%self.size 	
		if self.isFull:
			raise RuntimeError("Hash Table is Full")
		elif i < 100*self.size:
			self.hashtable[hashval][0] = key
			self.hashtable[hashval][1] = value
			self.collisions[hashval] = i
		else:
			self.unable_to_set +=1
			# raise RuntimeError("Unable to set item")


	def delete_item(self, key):
		i=0
		hashval = (hash_func(key) + i*probing_hash(key))%self.size 
		while self.hashtable[hashval][0] != key and i < self.size:
			i+=1
			hashval = (self.hash_func(key) + i*probing_hash(key))%self.size 
		if i < self.size:
			self.hashtable[hashval][1] = None
			self.hashtable[hashval][0] = "DEL"	
		else:
			raise RuntimeError("Unable to delete item")


	def __(self):
	    for entry in self.hashtable:
	    	if entry[0] != None:
	    		yield entry[0]

	@property
	def keys(self):
		return [entry[0] for entry in self.hashtable if entry[0] not in [None, "DEL"]]

	@property
	def values(self):
	    return [entry[1] for entry in self.hashtable if entry[0] not in [None, "DEL"]]
	
	@property
	def length(self):
	    return len(self.keys)

	@property
	def isFull(self):
	    return (self.length==self.size)

	
def test_univ_hash(size, hash_func, probing_hash):
	newHash = UniversalHash(size, hash_func, probing_hash)
	i=0
	with open('names_nums.txt', 'r') as f:
		#while i < size-1:
		for line in f.readlines():
			if i == size-1:
				break
			idnum, name = line.strip().split('|')[0], line.strip().split('|')[1]  
			print("SETTING %s"%idnum)
			newHash[int(idnum)] = name
			i+=1
	sum_collisions = sum(newHash.collisions)
	return sum_collisions, newHash.unable_to_set
	

if __name__ == '__main__':
#arguments should be the size of the hash table
		#hash_size = sys.argv[1]
		#print("Hash table size will be %s"%hash_size)

		print(test_univ_hash(10))
#Now need to get a random input file and hash it
#then need to keep track of how many collisions there are
#time how long it takes to hash the file

# Need a program that tracks time and then plots it 

	