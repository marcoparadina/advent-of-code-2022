# Day 4 of advent code

# example inputs
f = open('input.txt', 'r')

# https://stackoverflow.com/questions/32480423/how-to-check-if-a-range-is-a-part-of-another-range-in-python-3-x
def range_subset(range1, range2):
    """Whether range1 is a subset of range2."""
    if not range1:
        return True  # empty range is subset of anything
    if not range2:
        return False  # non-empty range can't be subset of empty range
    if len(range1) > 1 and range1.step % range2.step:
        return False  # must have a single value or integer multiple step
    return range1.start in range2 and range1[-1] in range2

def range_overlap(range1, range2):
    """Whether range1 is a subset of range2."""
    if not range1:
        return True  # empty range is subset of anything
    if not range2:
        return False  # non-empty range can't be subset of empty range
    if len(range1) > 1 and range1.step % range2.step:
        return False  # must have a single value or integer multiple step
    return range1.start in range2 or range1[-1] in range2

def getRange(line):
    new_line = line.split(',')
    line1 = new_line[0]
    line2 = new_line[1]
    num1 = line1.split('-')[0]
    num2 = line1.split('-')[1]
    num3 = line2.split('-')[0]
    num4 = line2.split('-')[1]
    return range(int(num1), int(num2)+1), range(int(num3), int(num4)+1)
    # +1 beacause, last int of range is not included with range()
    # with this puzzle, you need to consider all integers
    # perhaps, using range was not best way


lines = f.readlines()
count = 0
# check fully contain (part one)
# for line in lines:
#     range1, range2 = getRange(line)
#     if range_subset(range1, range2) == True or range_subset(range2, range1) == True:
#         count += 1

# check overlap (part two)
for line in lines:
    range1, range2 = getRange(line)
    if range_overlap(range1, range2) == True or range_subset(range2, range1) == True:
        count += 1


print(count)
f.close()
