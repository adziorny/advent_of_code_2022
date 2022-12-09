# Read the input file
f = open("day02-input.txt", "r")

ss = 0

# Part 1
# ------
# for x in f:

#     if x[0] == 'A': # Rock
#         if x[2] == 'X': # Rock == 1
#             ss += 1 + 3
#         elif x[2] == 'Y': # Paper == 2
#             ss += 2 + 6
#         elif x[2] == 'Z': # Sissors == 3
#             ss += 3 + 0
#         else:
#             print('Error! x =',x)

#     elif x[0] == 'B': # Paper
#         if x[2] == 'X': # Rock == 1
#             ss += 1 + 0
#         elif x[2] == 'Y': # Paper == 2
#             ss += 2 + 3
#         elif x[2] == 'Z': # Sissors == 3
#             ss += 3 + 6
#         else:
#             print('Error! x =',x)

#     elif x[0] == 'C': # Sissors
#         if x[2] == 'X': # Rock == 1
#             ss += 1 + 6
#         elif x[2] == 'Y': # Paper == 2
#             ss += 2 + 0
#         elif x[2] == 'Z': # Sissors == 3
#             ss += 3 + 3
#         else:
#             print('Error! x =',x)

#     else:
#         print('Error! x=',x)

#     #print('Score:',ss,'X:',x)

# print('Sum score:',ss)

for x in f:

    # Rock = 1
    # Paper = 2
    # Sissors = 3

    if x[0] == 'A': # Rock
        if x[2] == 'X': # Lose
            ss += 3 + 0
        elif x[2] == 'Y': # Draw
            ss += 1 + 3
        elif x[2] == 'Z': # Win
            ss += 2 + 6
        else:
            print('Error! x =',x)

    elif x[0] == 'B': # Paper
        if x[2] == 'X': # L
            ss += 1 + 0
        elif x[2] == 'Y': # D
            ss += 2 + 3
        elif x[2] == 'Z': # W
            ss += 3 + 6
        else:
            print('Error! x =',x)

    elif x[0] == 'C': # Sissors
        if x[2] == 'X': # L
            ss += 2 + 0
        elif x[2] == 'Y': # D
            ss += 3 + 3
        elif x[2] == 'Z': # W
            ss += 1 + 6
        else:
            print('Error! x =',x)

    else:
        print('Error! x=',x)

    print('Score:',ss,'X:',x)

print('Sum score:',ss)