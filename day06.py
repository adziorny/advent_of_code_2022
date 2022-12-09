# Read the input file
f = open("day06-input.txt", "r")

desired_len = 14

print('desired len:',desired_len)

for x in f:

    print('len:',len(x))

    for i in range(len(x)):

        if i < (desired_len - 1): 
            print('start:',x[0:i+5],'x[i]:',x[i],'i:',i,'pos:',i+1)

            continue

        my_set = set()
        
        for j in range(desired_len):
            my_set.add(x[i-j])

        if len(my_set) == desired_len:

            print('set:',my_set,'i:',i,'pos:',i+1)

        # if x[i-3] != x[i-2] and x[i-3] != x[i-1] and x[i-3] != x[i] and \
        #     x[i-2] != x[i-1] and x[i-2] != x[i] and \
        #         x[i-1] != x[i]:

        #     print('str:',x[i-3:i+1],'i:',i,'pos:',i+1)

        #     print('re-print set:',my_set)

        #     break
