"""
For visualizer to work, use:
- lst[index].getValue()  -  To access elements of the given list
- lst[index].setValue(new_value)  -  To change elements of the given list

- Do not change the name of the `main` function.
"""

def main(lst):
	# Traverse through 1 to len(lst)
	for i in range(1, len(lst)):

		key = lst[i].getValue()

		# Move elements of lst[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		j = i - 1
		while j >= 0 and key < lst[j]:
			lst[j + 1].setValue(lst[j])
			j -= 1
		lst[j + 1].setValue(key)
