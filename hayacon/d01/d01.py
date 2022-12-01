# Day 01 of advent of code 2022!!

f = open('input.txt', 'r')

totalCalories = 0
elvesCalories = []

lines = f.readlines()
for line in lines:
    if line == '\n':
        elvesCalories.append(totalCalories)
        totalCalories = 0
        continue
    else:
        totalCalories += int(line)

elvesCalories.sort(reverse=True)
print(elvesCalories[0] + elvesCalories[1] + elvesCalories[2])
f.close()
