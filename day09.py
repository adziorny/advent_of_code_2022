def moveTail (old_Tx, old_Ty, new_Hx, new_Hy):
    """
    Move the tail based on the head old and new positions
    """

    # First cover the time when they are covering - this is fine, don't move
    if old_Tx == new_Hx and old_Ty == new_Hy:
        return old_Tx, old_Ty

    # Now cover the time when they are one away linearly - this is also fine
    if abs(old_Tx - new_Hx) == 1 and old_Ty == new_Hy:
        return old_Tx, old_Ty

    if old_Tx == new_Hx and abs(old_Ty - new_Hy) == 1:
        return old_Tx, old_Ty

    # If they are one away diagonally - this is also fine
    if abs(old_Tx - new_Hx) == 1 and abs(old_Ty - new_Hy) == 1:
        return old_Tx, old_Ty

    # Now cover them being 2 away linearly - move to one away
    if old_Tx - new_Hx == 2 and old_Ty == new_Hy:
        return old_Tx-1, old_Ty
    
    if new_Hx - old_Tx == 2 and old_Ty == new_Hy:
        return old_Tx+1, old_Ty

    if old_Tx == new_Hx and old_Ty - new_Hy == 2:
        return old_Tx, old_Ty-1

    if old_Tx == new_Hx and new_Hy - old_Ty == 2:
        return old_Tx, old_Ty+1

    # Lastly, cover the diagonals - move diagonal to make up the difference
    # This one has the most possibilities

    # Start with the two away on the x - can either be above or below, two ahead or behind
    if abs(old_Tx - new_Hx) == 2 and abs(old_Ty - new_Hy) == 1:
        # move to the same row (Y), one X closer
        if old_Tx < new_Hx:
            return old_Tx+1, new_Hy
        else:
            return old_Tx-1, new_Hy

    # Now look for two away on the y - can either be left or right, two above or below
    if abs(old_Tx - new_Hx) == 1 and abs(old_Ty - new_Hy) == 2:
        # move to the same col (X), one Y closer
        if old_Ty < new_Hy:
            return new_Hx, old_Ty+1
        else:
            return new_Hx, old_Ty-1

    # In Part 2, we add another complication ... both row and col can be 2 away, and we move to one away
    if abs(old_Tx - new_Hx) == 2 and abs(old_Ty - new_Ty) == 2:
        
        # Move closer to new
        if old_Tx < new_Hx and old_Ty < new_Ty:
            return old_Tx+1, old_Ty+1
        elif old_Tx < new_Hx and old_Ty > new_Ty:
            return old_Tx+1, old_Ty-1
        elif old_Tx > new_Hx and old_Ty < new_Ty:
            return old_Tx-1, old_Ty+1
        else:
            return old_Tx-1, old_Ty-1

    print('*** Should never get here!! old_Tx:',old_Tx,'old_Ty:',old_Ty,'new_Hx:',new_Hx,'new_Hy:',new_Hy)

# Debug with the example trail
#print(moveTail(3, 0, 4, 1, 'U'))
#print(moveTail(3, 0, 4, 2, 'U'))
#print(moveTail(4, 1, 4, 3, 'U'))
#print(moveTail(4, 2, 4, 4, 'U'))
#print(moveTail(4, 3, 3, 4, 'L'))
#print(moveTail(4, 3, 2, 4, 'L'))

#exit()


def moveHead (dir, old_Hx, old_Hy):
    """
    Move the head based on the direction
    """

    if dir == 'U':
        new_Hx = old_Hx
        new_Hy = old_Hy + 1
    elif dir == 'D':
        new_Hx = old_Hx
        new_Hy = old_Hy - 1
    elif dir == 'R':
        new_Hx = old_Hx + 1
        new_Hy = old_Hy
    elif dir == 'L':
        new_Hx = old_Hx - 1
        new_Hy = old_Hy
    else:
        print('*** Error: direction does not match')

    return new_Hx, new_Hy

# Read the input file
#f = open("day09-input-short.txt", "r")
f = open("day09-input.txt", "r")

# Each element in trail will have 5-element list
# [index, Hx, Hy, Tx, Ty]
trail = []

# Start at head
trail.append([0, 0, 0, 0, 0])

# For each row in input ...
for x in f:

    dir = x[0]
    mag = int(x[2:len(x.strip())].strip())

    # For each step in magnitude ...
    for i in range(mag):

        last = trail[-1]

        old_Hx = last[1]
        old_Hy = last[2]

        new_Hx, new_Hy = moveHead(dir, old_Hx, old_Hy)

        new_Tx, new_Ty = moveTail(last[3], last[4], new_Hx, new_Hy)

        new_ind = last[0] + 1
        trail.append([new_ind, new_Hx, new_Hy, new_Tx, new_Ty])

        #print('Original:',last,'Dir:',dir,'Mag:',mag,'New:',trail[-1])

f.close()

# Now we have a complete list of all places covered by the tail - add them to a set, and count
tail_unique = set()

# Now add all new spaces
for spot in trail:

    # Add as a string "x,y" because lists are unhashable
    tail_unique.add( str(spot[3])+","+str(spot[4]) )

print('Len of trail:',len(trail),'Count of cells in tail_unique:',len(tail_unique))

# Part 2
import copy

# Read the input file
#f = open("day09-input-short.txt", "r")
f = open("day09-input.txt", "r")

# Now each index into trail is a list of 10 x 2-element list, 
# where 10 is the number of knots and each knot has a 2-element position.
# The index is still the first element
rope_len = 10

trail = []

# Start at head
head = []
head.insert(0, 0)
for i in range(rope_len):
    head.insert(i+1, [0,0])
trail.append(head)

# For each line in input ...
for x in f:

    dir = x[0]
    mag = int(x[2:len(x.strip())].strip())

    # For each step in the magnitude:
    for i in range(mag):

        last = trail[-1]

        # Increment index
        old_ind = last[0]

        result = copy.deepcopy(last)

        result[0] = old_ind+1
        #result.insert(0,old_ind+1)

        # Move the head
        old_Hx = result[-1][0]
        old_Hy = result[-1][1]

        new_Hx, new_Hy = moveHead(dir, old_Hx, old_Hy)
        result[rope_len] = [new_Hx, new_Hy]

        # Then iteratively move each part of the rope
        # using the same `moveTail` method above
        for j in range(rope_len - 1): # j goes from 0 ... 8 (9 elements)

            prior_knot = result[rope_len-j]
            next_knot = result[rope_len-j-1]

            new_Tx, new_Ty = moveTail(next_knot[0], next_knot[1], prior_knot[0], prior_knot[1])

            #print('\tj:',j,'prior:',prior_knot,'next:',next_knot,'new:',[new_Tx, new_Ty])

            result[rope_len-j-1] = [new_Tx, new_Ty]

        trail.append(result)

        #print('dir:',dir,'mag:',mag,'result:',result)

f.close()

# Now we have a complete list of all places covered by the tail - add them to a set, and count
tail_unique = set()

# Now add all new spaces
for spot in trail:

    # Add as a string "x,y" because lists are unhashable
    tail_unique.add( str(spot[1][0])+","+str(spot[1][1]) )

print('Len of trail:',len(trail),'Count of cells in tail_unique:',len(tail_unique))
