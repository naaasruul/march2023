def getData():
    num1=int(input("number 1: "))
    num2=int(input("number 2: "))

    return ([num1,num2])

def calc(number):
    total = number[0]+number[1]
    return total

number = getData() # [5, 7]
print(number)

answer = calc(number)
print("total: ", answer)