"""
The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
 - Sort the list and find the min and max age
 - Add the min age and the max age again to the list
 - Find the median age (one middle item or two middle items divided by two)
 - Find the average age (sum of all items divided by their number )
 - Find the range of the ages (max minus min)
 - Compare the value of (min - average) and (max - average), use abs() method
"""

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25]

print(sorted(ages))
print(max(ages))
print(min(ages))

ages.append(max(ages))
ages.append(min(ages))
print(ages)

if len(ages) % 2 == 0:
    middle1 = ages[int(len(ages) / 2 - 1)]
    middle2 = ages[int(len(ages) / 2)]
    result = (middle1 + middle2) / 2
    print(result)
else:
    middle = ages[int(len(ages) / 2)]
    print(middle)

total = sum(ages)
average = total/len(ages)
print(average)

range = max(ages)-min(ages)
print(range)

print(abs(max(ages) - average) > abs(min(ages) - average))