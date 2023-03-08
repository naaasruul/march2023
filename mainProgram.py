def getNum():
    list = []
    for i in range(0,10):
        print("Enter number",i+1,":",end="")
        userInput = int(input())
        list.append(userInput)

    return list

def calcOdd(number):  #[1,2,3,4,5,6,7,7,4,3,3] #dah ada toral
    sum = 0
    for i in range(0,len(number)):
        if number[i] % 2 == 1:
            sum = sum + number[i]

    return sum

def calcEven(number):
    sum = 0
    for i in range(0,len(number)):
        if number[i] % 2 == 0:
            sum = sum + number[i]

    return sum

number = getNum() #[1,2,3,4,5,6,7,7,4,3,3]
totalOdd = calcOdd(number)
totalEven = calcEven(number)

print("total odd: ",totalOdd)
print("total even: ",totalEven)

    