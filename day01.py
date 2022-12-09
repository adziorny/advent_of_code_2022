# Read the input file
f = open("day01-input.txt", "r")

foodList = {}

elf = 1
foodList[elf] = 0
#foodList.insert(elf, 0)

for x in f:

    print('Elf:',elf,'X:',x)

    if len(x.strip()) == 0:
        elf = elf + 1
        foodList[elf] = 0
        #foodList.insert(elf, 0)
        continue

    foodList[elf] = foodList[elf] + int(x)

max_value = max(foodList, key=foodList.get)

print('Number of Elves:',elf)
print('Max food value:',foodList[max_value])
print('Index of max value:',max_value)

first_elf = foodList[max_value]
foodList[max_value] = 0

max_value = max(foodList, key=foodList.get)

print('Number of Elves:',elf)
print('Max food value:',foodList[max_value])
print('Index of max value:',max_value)

second_elf = foodList[max_value]
foodList[max_value] = 0

max_value = max(foodList, key=foodList.get)

print('Number of Elves:',elf)
print('Max food value:',foodList[max_value])
print('Index of max value:',max_value)

third_elf = foodList[max_value]

print('Sum:',first_elf+second_elf+third_elf)