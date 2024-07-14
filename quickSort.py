def quickSort(arr):
	if len(arr) <= 1:
		return arr
	else:
		pivot = len(arr) // 2
		left = [x for x in arr if x < arr[pivot]]
		middle = [x for x in arr if x == arr[pivot]]
		right = [x for x in arr if x > arr[pivot]]
		return quickSort(left) + middle + quickSort(right)


"""
Base Case: If the array length is 1 or less, it is already sorted, so return it.
Choose Pivot: Use the middle element of the array as the pivot.
Partitioning:
left: All elements less than the pivot.
middle: All elements equal to the pivot.
right: All elements greater than the pivot.
Recursive Sorting: Recursively apply Quicksort to the left and right subarrays.
Combine: Concatenate the sorted left subarray, the middle subarray, and the sorted right subarray.

Time complexity: O(n*log(n)) 
Average Space complexity (in-place): O(log(n))
Average Space complexity (not in-place): O(n)
"""

