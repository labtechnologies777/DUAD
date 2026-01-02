def reverse_bubble_sort(list_to_sort):
	for repetition in range(len(list_to_sort)):
		for index in range(len(list_to_sort) - 1 , repetition , -1):
			current_number = list_to_sort[index]
			next_number = list_to_sort[index - 1]
			if current_number > next_number:
				list_to_sort[index] = next_number
				list_to_sort[index - 1] = current_number
		
	return list_to_sort

