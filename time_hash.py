#Test time and number of collisions for hash
import timeit
import universalhash




if __name__ == '__main__':

	t = timeit.Timer("universalhash.test_univ_hash(1000)", "import universalhash")
	result = t.timeit()
	print("Total time is %s"%result)

	