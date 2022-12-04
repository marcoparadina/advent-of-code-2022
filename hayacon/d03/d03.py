# Day 3 of advent code !!

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

# convert charcter to integer based on above instruction
def convertCharToInt(char):
    if char.isupper():
        return(ord(char) - 38)
    elif char.islower():
        return(ord(char) - 96)
    else:
        return(0)

f = open("input.txt", "r")
lines = f.readlines()
sum = 0

# part one
# for line in lines:
#     # print(len(line))
#     s = int((len(line)-1)/2)
#     l = ' '
#     p = ' '
#     for i in range(s):
#         l += line[i]
#         p += line[i+s]
#     # removing duplicate characters
#     p = "".join(set(p))
#
#     for i in p:
#         print(l)
#         if i in l:
#             sum += convertCharToInt(i)

# part two
for i in range(0, len(lines), 3):
    bag1 = "".join(set(lines[i]))
    bag2 = "".join(set(lines[i+1]))
    bag3 = "".join(set(lines[i+2]))
    for i in bag1:
        if i in bag2 and i in bag3:
            sum += convertCharToInt(i)


print(sum)
f.close()
