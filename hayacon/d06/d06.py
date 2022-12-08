# Day 6 of advent code

# this algortihm is very bad O(n^2)
def duplicate(s):
    for i in range(len(s)):
        chr = s[i]
        for j in range(len(s)):
            if i == j:
                continue
            elif s[j] == chr:
                # print('True')
                return True
            else:
                continue
    # print('false')
    return False




f = open('input.txt', 'r')

line = f.readline()

count = 13
for i in range(len(line)):
    # print(count)
    count += 1
    s = ''
    for j in range(14):
        s = s + line[i+j]
    print(s)
    if duplicate(s) == True:
        continue
    else:
        break


print(count)


f.close()
