f = open('input.txt', 'r')
code = []
code = f.read().split('\n')

newCode = []
for i in code:
    newCode.append(i.split(' '))

def solver(opp, me):
    if opp == me:
        return 0
    elif opp == 'rock':
        if me == 'paper':
            return 2 + 6
        else:
            if me == 'scissors':
                return 