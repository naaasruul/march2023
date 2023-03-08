# {1: -10,2: -8, 3: -6, 4:-4, 5:-2,}

i = -10
number = []
data = {}
count = 0

while i < -1:
    number.append(i)
    data[count+1] = number[count] #   masuk kan dalam dictionary
    i = i + 2 #
    count = count + 1

print(data)