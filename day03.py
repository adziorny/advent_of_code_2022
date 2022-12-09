# Read the input file
f = open("day03-input.txt", "r")

# Part 1
""" ss = 0

for x in f:
 
    split = int(len(x.strip()) / 2)

    #print(split)

    top = x[0:split]
    bottom = x[split:len(x)]

    intersect = set(top).intersection(set(bottom))

    #print(x,' : ',top,' - ',bottom,' - ',intersect)

    if len(intersect) != 1:
        print('Error: intersect ',intersect,' is not == 1!')

    thisChar = next(iter(intersect))

    #print('char:',thisChar,'ascii:',ord(thisChar))

    asciiChar = ord(thisChar)

    if asciiChar >= 97 and asciiChar <= 122:
        numChar = asciiChar - 96

    if asciiChar >= 65 and asciiChar <= 90:
        numChar = asciiChar - 64 + 26

    print('char:',thisChar,'ascii:',asciiChar,'num:',numChar)

    ss += numChar

print('ss:',ss) """

all_lines = {}
index = 0
for x in f:
    all_lines[index] = x.strip()

    index += 1

num_groups = int(index / 3)

print('index:',index,'num_groups:',num_groups)

ss = 0

index = 0
for grp in range(num_groups):

    set_1 = all_lines[index]
    index += 1
    set_2 = all_lines[index]
    index += 1
    set_3 = all_lines[index]
    index += 1

    intersect = set(set_1).intersection(set(set_2)).intersection(set(set_3))

    print('grp:',grp,'intersect:',intersect)

    if len(intersect) != 1:
        print('Error: intersect ',intersect,' is not == 1!')

    thisChar = next(iter(intersect))

    asciiChar = ord(thisChar)

    if asciiChar >= 97 and asciiChar <= 122:
        numChar = asciiChar - 96

    if asciiChar >= 65 and asciiChar <= 90:
        numChar = asciiChar - 64 + 26

    print('char:',thisChar,'ascii:',asciiChar,'num:',numChar)

    ss += numChar

print('sum:',ss)