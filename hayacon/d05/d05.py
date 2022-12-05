# Day 5 of advent calender

#     [S] [C]         [Z]
# [F] [J] [P]         [T]     [N]
# [G] [H] [G] [Q]     [G]     [D]
# [V] [V] [D] [G] [F] [D]     [V]
# [R] [B] [F] [N] [N] [Q] [L] [S]
# [J] [M] [M] [P] [H] [V] [B] [B] [D]
# [L] [P] [H] [D] [L] [F] [D] [J] [L]
# [D] [T] [V] [M] [J] [N] [F] [M] [G]
#  1   2   3   4   5   6   7   8   9

stacks = [['D', 'L', 'J', 'R', 'V', 'G', 'F'],
          ['T', 'P', 'M', 'B', 'V', 'H', 'J', 'S'],
          ['V', 'H', 'M','F','D','G','P','C'],
          ['M','D','P','N','G','Q'],
          ['J','L','H','N','F'],
          ['N','F','V','Q','D','G','T','Z'],
          ['F','D','B','L'],
          ['M','J','B','S','V','D','N'],
          ['G','L','D'],]


f = open('input.txt', 'r')
lines = f.readlines()

def printStack(stacks):
    for stack in stacks:
        print(stack)
    print('\n')
printStack(stacks)

# input example
# move 2 from 8 to 3
for line in lines:
    line = line.split(' ')
    _move = int(line[1])
    _from = int(line[3]) - 1
    _to = line[5].replace('\n','')
    _to = int(_to) - 1

    # Part One
    # for i in range(_move):
        # top = stacks[_from].pop()
        # stacks[_to].append(top)
    # Part Two
    stacks[_from].reverse()
    items = stacks[_from][0:_move]
    items.reverse()
    stacks[_to].extend(items)
    del stacks[_from][0:_move]
    stacks[_from].reverse()

printStack(stacks)
for stack in stacks:
    print(stack[-1])

f.close()
