# day 2 of adevent code
# A : Rock  B : Paper  C : Scissors
# X : Rock  Y : Paper  Z = Scissors
# score for shape  1 : Rock  2 : Paper  3 : Scissors
# score for outcome of the round  0 : Lost  3 : Draw  6 : Won

f = open('input.txt', 'r')
# result is shown on index 0(opponent) and 2(you)

totalScore = 0

lines = f.readlines()

# part 1
# for l in lines:
#     # score
#     if l[2] == 'X':
#         totalScore += 1
#         if l[0] == 'A':
#             totalScore += 3
#         elif l[0] == 'B':
#             totalScore += 0
#         elif l[0] == 'C':
#             totalScore += 6
#         else:
#             print('error')
#             break
#
#     elif l[2] == 'Y':
#         totalScore += 2
#         if l[0] == 'A':
#             totalScore += 6
#         elif l[0] == 'B':
#             totalScore += 3
#         elif l[0] == 'C':
#             totalScore += 0
#         else:
#             print('error')
#             break
#
#     elif l[2] == 'Z':
#         totalScore += 3
#         if l[0] == 'A':
#             totalScore += 0
#         elif l[0] == 'B':
#             totalScore += 6
#         elif l[0] == 'C':
#             totalScore += 3
#         else:
#             print('error')
#             break
#     else:
#         print('error')
#         break

# part 2
# action requirment  X : to lose  Y : to draw  Z : to win

for l in lines:
    # score
    if l[2] == 'X':  # to lose
        totalScore += 0
        if l[0] == 'A':
            totalScore += 3
        elif l[0] == 'B':
            totalScore += 1
        elif l[0] == 'C':
            totalScore += 2
        else:
            print('error')
            break

    elif l[2] == 'Y': # to draw
        totalScore += 3
        if l[0] == 'A':
            totalScore += 1
        elif l[0] == 'B':
            totalScore += 2
        elif l[0] == 'C':
            totalScore += 3
        else:
            print('error')
            break

    elif l[2] == 'Z': # to win
        totalScore += 6
        if l[0] == 'A':
            totalScore += 2
        elif l[0] == 'B':
            totalScore += 3
        elif l[0] == 'C':
            totalScore += 1
        else:
            print('error')
            break
    else:
        print('error')
        break

print(totalScore)

f.close()
