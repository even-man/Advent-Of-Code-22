# import string as str

# cals = []

# with open('input.txt', 'r') as f:
# 	cals = f.read().split('\n\n')
# 	for string in cals:
# 		elfTotals = string.replace('\n', ' ')
# 		elfTotalsSplit = elfTotals.split('\n')
	
	
f = open('input.txt', 'r')

cals = f.read().split('\n\n')
calsClean = []
for i in cals:
	calsClean.append(i.replace('\n', ' '))

# print(calsClean)
calsCleanNew = []
for i in calsClean:
	calsCleanNew.append(i.split(' '))

totals = []
innerTotal = 0
for elf in calsCleanNew:
	for num in elf:
		innerTotal += int(num)
	totals.append(innerTotal)
	innerTotal = 0

currGreatest = 0
for total in totals:
	if total > currGreatest:
		currGreatest = total

print(f"top elf: {currGreatest}")

totals.sort(reverse=True)

topThree = totals[0] + totals[1] + totals[2]
print(f"topThree Total: {topThree}")