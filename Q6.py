import math

C = 50
H = 30
user_input = input("Pleaase type Comma seprated values: ")
user_list = user_input.split(',')
d = [int(num) for num in user_list]
r = [round(math.sqrt((2*C*i)/H)) for i in d]
print(r)


#for i in d:
 #   q = (2*C*i)/H

  #  r.append(round(q))

#print(r)

#result = [round(num) for num in r]
#print(result)
#i=0
#while i <= len(d):
 #   q = (2*C*d)/H
  #  print(q)
   # i+=i


