for i in range(151): #Question 1
    print(i)

for x in range(5, 1001, 5): #Question 2
    print(x)

for y in range(1, 100): #Question 3
    if y % 5 == 0:
        print('Coding')
    if y % 10 == 0:
        print('Dojo')
    else:
        print(y)

finalSum = 0 #Question 4
for q in range(0, 500000):
    if q % 2 != 0:
        finalSum += q
print(finalSum)

for z in range(2018, 0, -4): #Question 5
    print(z)

lowNum = 2 #Question 6
highNum = 10
for a in range(lowNum, highNum):
    mult = a
    if mult % 3 == 0:
        print(mult)