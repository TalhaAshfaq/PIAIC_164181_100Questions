binary_digit = []
j = 0
i = 'a'
while i != 's':
    i = input("Enter 4 digit binary number or type s to stop: ")
    if i == '1010' or i == '0101':
        binary_digit.append(i)
    j+=1

print(f"The numbers that are divisible by 5 are: {binary_digit}")
