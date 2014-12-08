#Test time and number of collisions for hash
import timeit
from universalhash import hash_func, probing_hash, linear_probing, quadratic_probing, test_univ_hash, funcs
#import universalhash



if __name__ == '__main__':
	coll_err_time = dict()
	
	for i, probfnc in enumerate(funcs):
		collision, errors = test_univ_hash(100, hash_func=hash_func, probing_hash=probfnc)
		print(funcs[i])
		t = timeit.Timer("test_univ_hash(10, hash_func = hash_func, \
			probing_hash=probfnc_index)",
		 "from universalhash import hash_func, probing_hash, linear_probing, quadratic_probing,\
		  test_univ_hash, funcs; probfnc_index=funcs[%i]"%(i))
		result = t.repeat(1, 2)
		print("Total time is %s"%max(result))
		coll_err_time[probfnc] = [collision, errors, max(result)]

	for key, item in coll_err_time.items():
		print("Function is %s"%key)
		print("Collisions, errors, max time is %s, %s, %s"%(item[0], item[1], item[2]))


	