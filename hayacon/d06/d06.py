# Day 6 of advent code

# this algortihm is very bad O(n^2)
def duplicate(s):
    for i in range(len(s)):
        chr = s[i]
        for j in range(len(s)):
            if i == j:
                continue
            elif s[j] == chr:
                return True
            else:
                continue
    return False




f = open('input.txt', 'r')

line = f.readline()

count = 13
for i in range(len(line)):
    count += 1
    s = ''
    # part 1
    # for j in range(4):
    #     s = s + line[i+j]
    # part 2
    for j in range(14):
        s = s + line[i+j]
    print(s)
    if duplicate(s) == True:
        continue
    else:
        break


print(count)


f.close()
