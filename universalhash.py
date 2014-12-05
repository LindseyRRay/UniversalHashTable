#in universal hashing, a random function from a family of hash functions is chosen

#let p = max of possible keys and also prime
#let a is a random number from 0 to 1, and b is any number between o and p-1
#hashf(a,b))(k) = ((ak+b)%p)%m) where m is length of hash table


def isprime(n):
	if n <= 2 or n%2 == 0:
		return False
	return not any((n%i==0 for i in range(3,n-1)))


