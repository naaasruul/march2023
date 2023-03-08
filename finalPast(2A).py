def calculate(num):
    print(sum(num))

number = [] #2,4,6,8

for count in range(1,10,2):
    number.append(count)

answer = calculate(number)

count = 1

for data in number:
    print(count, ":",data)
    count = count + 1

print("Answer: ",end="")
print(answer)
