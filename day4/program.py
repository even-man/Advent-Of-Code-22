f = open('input.txt', 'r')
assignments = f.read().splitlines()

total = 0

#SOLUTION PART 1
#splits parts of data into different variables, compares variables to find 

# for item in assignments:

#     first, last = item.split(',')
#     firstLow, firstHigh = first.split('-')
#     lastLow, lastHigh = last.split('-')
    
#     # print(firstLow, firstHigh, lastLow, lastHigh)

#     if ((int(firstLow) <= int(lastLow)) and (int(firstHigh) <= int(lastHigh))) or ((int(lastLow) <= int(firstLow)) and (int(lastHigh) <= int(firstHigh))):
#         total += 1

# print(f'total : {total}')
t = 0

for i in assignments:

    a,b=i.split(",")

    aa, aaa = [int(r) for r in a.split("-")]
    bb, bbb = [int(r) for r in b.split("-")]
    
    print(a, b, aa, aaa, bb, bbb)

    if (aa <= bb and aaa >= bbb ) or (bb<=aa and bbb>=aaa):
        t+=1


print(t)