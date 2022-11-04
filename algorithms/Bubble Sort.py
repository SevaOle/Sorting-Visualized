"""
For visualizer to work, use:
- lst[index].getValue()  -  To access elements of the given list
- lst[index].setValue(new_value)  -  To change elements of the given list

- Do not change the name of the `main` function.
"""

def main(lst):
	n = len(lst)
	# Traverse through all array elements
	for i in range(n - 1):
		# range(n) also work but outer loop will
		# repeat one time more than needed.

		# Last i elements are already in place
		for j in range(0, n - i - 1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if lst[j] > lst[j + 1]:
				buffer = lst[j].getValue()
				lst[j].setValue(lst[j + 1].getValue())
				lst[j + 1].setValue( buffer )
	return lst