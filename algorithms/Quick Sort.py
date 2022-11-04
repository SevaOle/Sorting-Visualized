"""
For visualizer to work, use:
- lst[index].getValue()  -  To access elements of the given list
- lst[index].setValue(new_value)  -  To change elements of the given list

- Do not change the name of the `main` function.
"""

def partition(lst, low, high):
	i = (low - 1)  # index of smaller element
	pivot = lst[high].getValue()  # pivot

	for j in range(low, high):

		# If current element is smaller than or
		# equal to pivot
		if lst[j] <= pivot:
			# increment index of smaller element
			i = i + 1
			buffer = lst[i].getValue()
			lst[i].setValue(lst[j])
			lst[j].setValue(buffer)

	buffer = lst[i+1].getValue()
	lst[i+1].setValue(lst[high])
	lst[high].setValue(buffer)
	return i + 1


def main(lst, low = None, high = None):
	low = 0 if low is None else low
	high = len(lst) - 1 if high is None else high
	if len(lst) == 1:
		return lst
	if low < high:
		# pi is partitioning index, lst[p] is now
		# at right place
		pi = partition(lst, low, high)

		# Separately sort elements before
		# partition and after partition
		main(lst, low, pi - 1)
		main(lst, pi + 1, high)