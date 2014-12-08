#generate random file of 1000 integers and chars

from random import randint, choice 
from string import ascii_letters

def gen_randoms(size):

	with open('names_nums.txt', 'w') as f:
		for i in range(10000):
			idNum = str(randint(1000,10000))
			name = ''.join([choice(ascii_letters) for x in range(10)])
			f.write(str(idNum)+'|'+name+'\n')

if __name__ == '__main__':

	gen_randoms(1000)
	