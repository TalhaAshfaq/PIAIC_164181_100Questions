user_input = input("Enter a sentences: ")
uppercase_letters = sum(1 for i in user_input if i.isupper())
print(f"Total uppercase letters in your sentence are: {uppercase_letters}")

lowercase_letters = sum(1 for i in user_input if i.islower())
print(f"Total lowercase letters in your sentence are: {lowercase_letters}")
