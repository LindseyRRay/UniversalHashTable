import universalhash


if __name__ == '__main__':

	print(universalhash.test_univ_hash(10, hash_func = universalhash.hash_func, probing_hash=universalhash.linear_probing))