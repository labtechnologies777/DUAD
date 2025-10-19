def reverse_bubble_sort(list_to_sort):
	for repetition in range(len(list_to_sort)):
		flag = False 
		for index in range(len(list_to_sort) - 1 , repetition , -1):
			current_number = list_to_sort[index]
			next_number = list_to_sort[index - 1]
			print(f"Repetition: {repetition} -- Index:{index} -- Current number: {current_number} -- Next number : {next_number} ")
			if current_number > next_number:
				print('El elemento actual es mayor al siguiente. Intercambiandolos...')
				list_to_sort[index] = next_number
				list_to_sort[index - 1] = current_number
				flag = True 
			
		if not flag:
			return

list_to_sort = [1, 8 , 10, 2, 7, 4, 9 ]
reverse_bubble_sort(list_to_sort)
print(list_to_sort)