#opening file and creating clean data
f = open('input.txt', 'r')
code = []
code = f.read().split('\n')

newCode = []
for i in code:
    newCode.append(i.split(' '))

#map
map = {
    'A':'rock',
    'B':'paper',
    'C':'scissors',
    'X':'rock',
    'Y':'paper',
    'Z':'scissors'
}

#solver for part 1 
def solver(opp, me):
    if opp == me:
        if me == 'rock':
            return 3 + 1
        elif me == 'paper':
            return 3 + 2
        elif me == 'scissors':
            return 3 + 3
    elif opp == 'rock':
        if me == 'paper':
            return 6 + 2
        else:
            if me == 'scissors':
                return 0 + 3
    elif opp == 'paper':
        if me == 'rock':
            return 0 + 1
        elif me == 'scissors':
            return 6 + 3
    elif opp == 'scissors':
        if me == 'rock':
            return 6 + 1
        elif me == 'paper':
            return 0 + 2

#solve for part 1
total = 0
for i in newCode:
    total += solver(map[i[0]], map[i[1]])

print(f"Part 1 Solution: {total}")

# X need to lose
# Y need to draw
# Z need to win

#solver for part two
def solverRefined(opp, outcome):
    #losing outcome
    if outcome == 'X':
        if opp == 'A':
            return 0 + 3
        elif opp == 'B':
            return 0 + 1
        elif opp == 'C':
            return 0 + 2
    #draw outcome
    elif outcome == 'Y':
        if opp == 'A':
            return 3 + 1
        elif opp == 'B':
            return 3 + 2
        elif opp == 'C':
            return 3 + 3
    #winning outcome
    elif outcome == 'Z':
        if opp == 'A':
            return 6 + 2
        elif opp == 'B':
            return 6 + 3
        elif opp == 'C':
            return 6 + 1


#solution for part 2
newTotal = 0
for i in newCode:
    newTotal += solverRefined(i[0], i[1])

print(f"Solution Part Two: {newTotal}")