# Read the input file
f = open("day04-input.txt", "r")

def start_end (s, substr):

    pos = s.find(substr)

    return s[0:pos], s[pos+1:len(s)]

cnt = 0
enc = 0
ovl = 0

for x in f:

    cnt += 1

    elf_1, elf_2 = start_end(x, ',')
    
    #pos = x.find(',')

    #elf_1 = x[0:pos]
    #elf_2 = x[pos+1:len(x)]

    #print('x:',x,'1:',elf_1,'2:',elf_2)

    s_1, e_1 = start_end(elf_1, '-')

    s_2, e_2 = start_end(elf_2, '-')

    s_1 = int(s_1)
    s_2 = int(s_2)
    e_1 = int(e_1)
    e_2 = int(e_2)

    print('x:',x.strip(),'1: ',int(s_1),'-',int(e_1),' 2:',int(s_2),'-',int(e_2))

    if (s_2 >= s_1 and e_2 <= e_1) or (s_1 >= s_2 and e_1 <= e_2):
        print('**** enclosed ****')

        enc += 1

    if (s_2 <= e_1 and s_2 >= s_1) or (s_1 <= e_2 and s_1 >= s_2):
        print('**** overlapped ****')

        ovl += 1

print('total:',cnt,' enclosed:',enc,' overlapped:',ovl)