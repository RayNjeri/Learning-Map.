
def done_list(studied_list, study_list):
    studied_list = []
    not_studied = []
    
    for item in study_list:
        if item not in study_list:
            print("Error in input")
            return studied_list, study_list
        else:
            study_list.remove(item)
            studied_list.append(item)
    return studied_list, study_list

studied_list = input("Enter the skills I've studied: ")
studied_list = studied_list.split(",")

print(done_list(studied_list, study_list))