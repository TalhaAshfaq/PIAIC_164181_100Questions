user_input = input("Enter comma seprated values: ")
user_list = user_input.split(',')
int_list = [int(i) for i in user_list]
print(int_list)

odd_list = [i**2 for i in int_list if i%2 != 0]
print("Squared odd numbers are: ",odd_list)
