"""
when we want do mathemtical operations for n dimensions arrays we can use numpy library where
it has many methods to process the matrices. libraries or frameworks will help you to avoid
messy code.
"""
import numpy as np

def update_less_100(a):
	""" for any value less 100 multiply it by 2 till there is no 
	element less than 100"""

	arr = a.copy()
	index_elements_less_100 = np.where(arr < 100)
	
	while index_elements_less_100[0].size:
		for index in np.nditer(index_elements_less_100[0]):
			arr[index] *= 2

		index_elements_less_100 = np.where(arr < 100)

	return arr
		

def get_between_150_200(arr):
	"""return elements in arr that 150 < element < 200"""
	great150 = 150 < arr;
	less200  = arr < 200
	return arr[great150 * less200]
	pass

def main():
	arr = np.array([230, 10, 284, 39, 76])
	print(get_between_150_200(update_less_100(arr)))
	pass

if __name__ == '__main__':
	main()