outPutList = []
for i in range(1000,3001):
    
    numberlist = [int(j) for j in str(i)]
    if numberlist[0]%2 == 0 and  numberlist[1]%2 == 0 and numberlist[2]%2 == 0 and numberlist[3]%2 == 0:
        outPutList.append(i)

print(outPutList)