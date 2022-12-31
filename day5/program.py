
#stack items
stack1 = ['D', 'T', 'R', 'B', 'J', 'L', 'W', 'G']
stack2 = ['S', 'W', 'C']
stack3 = ['R', 'Z', 'T', 'M']
stack4 = ['D', 'T', 'C', 'H', 'S', 'P', 'V']
stack5 = ['G', 'P', 'T', 'L', 'D', 'Z']
stack6 = ['F', 'B', 'R', 'Z', 'J', 'Q', 'C', 'D']
stack7 = ['S', 'B', 'D', 'J', 'M', 'F', 'T', 'R']
stack8 = ['L', 'H', 'R', 'B', 'T', 'V', 'M']
stack9 = ['Q', 'P', 'D', 'S', 'V']

#list of each stack, perhaps wouldve been better to just use a 2D array
stackList = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

#dict that maps stack number to the actual stack 
stacks = {
    1 : stack1,
    2 : stack2, 
    3 : stack3, 
    4 : stack4,
    5 : stack5,
    6 : stack6,
    7 : stack7,
    8 : stack8,
    9 : stack9
}

#file reading and manipulation of data to get a usable dataset
#final copy of data is a two dimensional list that contains three numbers in string format 
#for each instruction set
f = open('input.txt', 'r')
rawData = f.readlines()
instructions = list()
for item in rawData:
    instructions.append(item.replace('\n', ''))

finalInstructions = list()
for instruction in instructions:
    newItems = instruction.split(' ')
    finalInstructions.append(newItems)

for item in finalInstructions:
    for i in item:
        if i == 'from' or i == 'to' or i == 'move':
            item.remove(i)

#final data definitions:
#first Item: HOW MANY to move
#second item: where the items are being moved FROM
#third item: where the items are being moved TO

#algorithm goes through each instruction and pulls the details of each instruction
#then for howMany times, takes last item from movedFrom stack, deletes it from that stack
#and appends it to the movedTo stack
for line in finalInstructions:
    howMany = int(line[0])
    movedFrom = int(line[1])
    movedTo = int(line[2])

    for _ in range(howMany):
        lastItem = stacks[movedFrom][-1]
        del stacks[movedFrom][-1]
        stacks[movedTo].append(lastItem)

#print final stacks after manipulation
for i, stack in enumerate(stackList):
    print(i+1, end=' ')
    for item in stack:
        print( '[' + item + ']', end=' ')
    print()

for stack in stackList:
    print(stack[-1], end='')
