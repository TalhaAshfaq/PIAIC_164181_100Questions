
x, y = map(int, input("Enter two numbers separated by a comma (X,Y): ").split(','))

result = [[i * j for j in range(y)] for i in range(x)]

print(result)
