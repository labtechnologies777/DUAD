# def reverse_bubble_sort(list_to_sort):
# 	for repetition in range(len(list_to_sort)):  ## O(n)
# 		flag = False ## O(1)
# 		for index in range(len(list_to_sort) - 1 , repetition , -1):  ## O(n^2)
# 			current_number = list_to_sort[index] ## O(1)
# 			next_number = list_to_sort[index - 1] ## O(1)
# 			print(f"Repetition: {repetition} -- Index:{index} -- Current number: {current_number} -- Next number : {next_number} ") ## O(1)
# 			if current_number > next_number: ## O(1)
# 				print('El elemento actual es mayor al siguiente. Intercambiandolos...') ## O(1)
# 				list_to_sort[index] = next_number ## O(1)
# 				list_to_sort[index - 1] = current_number ## O(1)
# 				flag = True ## O(1)
			
# 		if not flag: ## O(1)
# 			return ## O(1)

# list_to_sort = [1, 8 , 10, 2, 7, 4, 9 ] ## O(1)
# reverse_bubble_sort(list_to_sort) ## O(1)
# print(list_to_sort) ## O(1)


## --------------------------------------------------------------------------------------

# def print_numbers_times_2(numbers_list): 
# 	for number in numbers_list: ## O(n)
# 		print(number * 2) ## O(1)



# def check_if_lists_have_an_equal(list_a, list_b): 
# 	for element_a in list_a:  ## O(n)
# 		for element_b in list_b: ## O(n^2)
# 			if element_a == element_b: ## O(1)
# 				return True ## O(1)
				
# 	return False  ## O(1)


# def print_10_or_less_elements(list_to_print):
# 	list_len = len(list_to_print) ## O(1)
# 	for index in range(min(list_len, 10)): ## O(1)
# 		print(list_to_print[index])  ## O(1)


# def generate_list_trios(list_a, list_b, list_c):
# 	result_list = [] ## O(1)
# 	for element_a in list_a: ## O(n)
# 		for element_b in list_b: ## (n^2)
# 			for element_c in list_c: ## (n^3)
# 				result_list.append(f'{element_a} {element_b} {element_c}') ## O(1)
				
# 	return result_list ## O(1)
