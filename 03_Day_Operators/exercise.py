import math

print(math.pi)

# _I hope this course is not full of jargon_. Use _in_ operator to check if _jargon_ is in the sentence.
sentence = 'I hope this course is not full of jargon'
i = 'jargon'
if i in sentence:
    print(True)
else:
    print(False)

'''
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''
num = 5
for i in range(1, 6):
    print(str(i) + ' ',end='')
    for j in range(0, 4):
        print(str(i ** j)+' ',end='')
    print('\n')