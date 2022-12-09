from anytree import Node, RenderTree

# Read the input file
f = open("day07-input.txt", "r")

lines = []

dtree = {}

for x in f:

    lines.append(x.strip())

print('# lines:',len(lines))

def parseCommand (lines, i, root, current):
    """
    lines[i] is a command line
    """

    cmd = lines[i].split()

    #print('\tcmd:',cmd)    

    if cmd[1] == 'cd':

        if cmd[2] == '/':

            return i+1, root, root

        if cmd[2] == '..':

            return i+1, root, current.parent

        for child in current.children:

            if child.name == cmd[2]:

                return i+1, root, child

        print('Error: could not find',cmd[1],'among child node names!')
        return

    if cmd[1] == 'ls':

        while True:

            i += 1
            nextLine = lines[i].split()

            if nextLine[0] == 'dir':

                #print('\t\tAdding new dir node:',nextLine[1])

                newNode = Node(nextLine[1], parent = current, type = 'dir')

            else:

                #print('\t\tAdding new file node:',nextLine[1],'size:',nextLine[0])

                newNode = Node(nextLine[1], parent = current, type = 'file', size = int(nextLine[0]))

            if i+1 >= len(lines):
                break

            if lines[i+1][0] == '$':
                break
            
        return i+1, root, current

i = 0
root = Node('root', type = 'dir')
current = root

while True:

    #print('i:',i,'lines[i]:',lines[i])

    if lines[i][0] == '$':
        i, root, current = parseCommand(lines, i, root, current)

    if i >= len(lines):
#        print(RenderTree(root))

        break

def collapseSize (n):

    size = 0
    
    for c in n.children:

        if c.type == 'dir':

            c = collapseSize(c)

            size += c.size

        else:
            size += c.size

    n.size = size

    return n

root = collapseSize(root)

#print(RenderTree(root))

# Part 1
def findSmallDirs (n, sizeSum):

    for c in n.children:

        if c.type == 'dir' and c.size <= 100000:

            #print('Included!',c)
            sizeSum += c.size

        if c.type == 'dir':
            sizeSum = findSmallDirs(c, sizeSum)

    return sizeSum

sizeSum = findSmallDirs(root, 0)

print('Size Sum:',sizeSum)

# Part 2
used_space = root.size
unused_space = 70000000 - used_space
needed_space = 30000000 - unused_space

print('Root size:',root.size)
print('Used:',used_space,'Unused:',unused_space,'Needed:',needed_space)

def findSizedDirs (n, minSize, minNode, goalMin):

    for c in n.children:

        #print('child name:',c.name,'size:',c.size)

        if c.type == 'dir' and c.size >= goalMin:

            print('\tMatch!',c)

            if c.size < minSize:
                minSize = c.size
                minNode = c

        if c.type == 'dir':

            minSize, minNode = findSizedDirs(c, minSize, minNode, goalMin)
    
    return minSize, minNode

minSize, minNode = findSizedDirs(root, minSize = 1000000000, minNode = '', goalMin = needed_space)

print('minSize:',minSize,'minNode:',minNode)