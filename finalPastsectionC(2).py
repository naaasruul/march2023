def getData():
    list = []
    for i in range(0,10,1):
        numInput = int(input(f"{i+1}."))
        list.append(numInput)
    return list

def largest_smallest(num):
    largest = max(num)
    smallest = min(num)
    return largest,smallest

def display(largest, smallest):
    print("largest number: ", largest)
    print("smallest number: ", smallest)

number = getData()
largest,smallest = largest_smallest(number)
display(largest,smallest)





