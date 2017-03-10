def done_list(studied_list):
	studied_list = list(input("Enter the skills I've studied: "))
	for item in study_list:
		for j in studied_list:
			if item == j:
				study_list.remove(item)
				studied_list.append(j)
				print(studied_list)
			else:
				print("item entered is not in our to do list")