def reverse_bubble_sort(list_to_sort):
	for repetition in range(len(list_to_sort)):  ## O(n)
		flag = False ## O(1)
		for index in range(len(list_to_sort) - 1 , repetition , -1):  ## O(n^2)
			current_number = list_to_sort[index] ## O(1)
			next_number = list_to_sort[index - 1] ## O(1)
			print(f"Repetition: {repetition} -- Index:{index} -- Current number: {current_number} -- Next number : {next_number} ") ## O(1)
			if current_number > next_number: ## O(1)
				print('El elemento actual es mayor al siguiente. Intercambiandolos...') ## O(1)
				list_to_sort[index] = next_number ## O(1)
				list_to_sort[index - 1] = current_number ## O(1)
				flag = True ## O(1)
			
		if not flag: ## O(1)
			return ## O(1)

list_to_sort = [1, 8 , 10, 2, 7, 4, 9 ] ## O(1)
reverse_bubble_sort(list_to_sort) ## O(1)
print(list_to_sort) ## O(1)