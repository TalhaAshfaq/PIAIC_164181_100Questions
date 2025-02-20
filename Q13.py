user_input = input("Enter a sentence that contain letters and digits: ")

letters = sum(1 for i in user_input if i.isalpha())
print("number of letters in sentence are: ", letters)

digits = sum(1 for i in user_input if i.isdigit())
print("number of digits in sentence are: ", digits)