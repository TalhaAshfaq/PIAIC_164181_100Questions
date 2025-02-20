user_input = input("Please enter a sentence: ")
user_list = user_input.split()

unique_elements = set(user_list)
sorted_list = sorted(unique_elements)
print(sorted_list)