# Read the input file
f = open("day05-input.txt", "r")

# Initialize the stacks
my_stacks = {
    1: ['R', 'N', 'P', 'G'],
    2: ['T', 'J', 'B', 'L', 'C', 'S', 'V', 'H'],
    3: ['T', 'D', 'B', 'M', 'N', 'L'],
    4: ['R', 'V', 'P', 'S', 'B'],
    5: ['G', 'C', 'Q', 'S', 'W', 'M', 'V', 'H'],
    6: ['W', 'Q', 'S', 'C', 'D', 'B' ,'J'],
    7: ['F', 'Q', 'L'],
    8: ['W', 'M', 'H', 'T', 'D', 'L', 'F', 'V'],
    9: ['L', 'P', 'B', 'V', 'M', 'J', 'F']
}

#print(my_stacks[9])

for x in f:

    cnt = int(x.split()[1])

    start = int(x.split()[3])

    end = int(x.split()[5])

    #print('x:',x.strip())
    print('cnt:',cnt,'start:',start,'end:',end)

    print('start:',my_stacks[start])
    print('end:',my_stacks[end])

    temp_list = []

    for i in range(cnt):
        temp_list.append(my_stacks[start].pop())
    
    for i in range(cnt):
        my_stacks[end].append(temp_list.pop())
    
    print('post start:',my_stacks[start])
    print('post end:',my_stacks[end])
    
my_str = ''

for key in my_stacks:

    print(my_stacks[key])
    print(my_stacks[key][-1])

    my_str += my_stacks[key][-1]

print('my_str:',my_str)