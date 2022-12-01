# Day 01 of advent of code 2022!!

f = open('input.txt', 'r')

theMostCalories = 0
totalCalories = 0

lines = f.readlines()
for line in lines:
    if line == '\n':
        if totalCalories > theMostCalories:
            theMostCalories = totalCalories
        else:
            theMostCalories = theMostCalories
        totalCalories = 0
        continue
    else:
        totalCalories += int(line)

print(theMostCalories)


f.close()
