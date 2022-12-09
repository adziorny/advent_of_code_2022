import numpy as np

# Read the input file
f = open("day08-input.txt", "r")

grid = []

for x in f:
    grid.append(x.strip())

print('rows:',len(grid),'cols:',len(grid[0]))

mask_size = (len(grid), len(grid[0]))
mask = np.zeros(mask_size, dtype=int)

#print('grid:',)

# by row first
for row in range(len(grid)):

    if (row == 0) or (row == len(grid)-1):
        mask[row,:] = 1
        continue

    # First from the left
    maxHeight = grid[row][0]

    ind = 1
    while ind < len(grid):


        if grid[row][ind] > maxHeight:
            mask[row,ind] = 1
            maxHeight = grid[row][ind]
            ind += 1
            continue
        elif grid[row][ind] <= maxHeight:
            ind += 1
            continue

        if maxHeight == 9:
            break

    # Now from the right
    maxHeight = grid[row][-1]

    ind = len(grid)-2
    while ind >= 0:

        if grid[row][ind] > maxHeight:
            mask[row,ind] = 1
            maxHeight = grid[row][ind]
            ind -= 1
            continue
        elif grid[row][ind] <= maxHeight:
            ind -= 1
            continue        

        if maxHeight == 9:
            break

# by column now
for col in range(len(grid[0])):

    if (col == 0) or (col == len(grid[0])-1):
        mask[:,col] = 1
        continue

    # First from the top
    maxHeight = grid[0][col]

    ind = 1
    while ind < len(grid[0]):

        if grid[ind][col] > maxHeight:
            mask[ind,col] = 1
            maxHeight = grid[ind][col]
            ind += 1
            continue
        elif grid[ind][col] <= maxHeight:
            ind += 1
            continue     

        if maxHeight == 9:
            break

    # Now from bottom
    maxHeight = grid[-1][col]

    ind = len(grid[0])-2
    while ind >= 0:

        if grid[ind][col] > maxHeight:
            mask[ind,col] = 1
            maxHeight = grid[ind][col]
            ind -= 1
            continue
        elif grid[ind][col] <= maxHeight:
            ind -= 1
            continue          

        if maxHeight == 9:
            break

print('mask:',mask)

print('sum:',np.sum(mask))

f = open("day08-output.txt", "w")

for i in range(len(grid)):
    f.write(np.array2string(mask[i,:], separator='', max_line_width=110)+'\n')

f.close()

# Part 2
def calculateScenicScore (r, c, grid):
    """
    Calculates the scenic score and returns the int value
    """

    # Go up first
    s_up = 0
    ind = r-1
    while ind >= 0:
        if grid[ind][c] < grid[r][c]:
            s_up += 1
            ind -= 1
            continue
        else:
            s_up += 1
            break

    # Go down
    s_down = 0
    ind = r+1
    while ind < len(grid):
        if grid[ind][c] < grid[r][c]:
            s_down += 1
            ind += 1
            continue
        else:
            s_down += 1
            break

    # Go left
    s_left = 0
    ind = c-1
    while ind >= 0:
        if grid[r][ind] < grid[r][c]:
            s_left += 1
            ind -= 1
            continue
        else:
            s_left += 1
            break

    # Go right
    s_right = 0
    ind = c+1
    while ind < len(grid[0]):
        if grid[r][ind] < grid[r][c]:
            s_right += 1
            ind += 1
            continue
        else:
            s_right += 1
            break
        
    return (s_up * s_down * s_left * s_right)

# Debug a sample tree
#print('2,96:',calculateScenicScore(96,2,grid))

maxScore = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if mask[r,c] == 1:

            scenic_score = calculateScenicScore(r,c,grid)

            if scenic_score > maxScore:

                maxScore = scenic_score

print('max Score:',maxScore)
