import pandas

print('### for ###')
for i in range(11):
    if i == 10:
        print(i)
    else:
        print(i, end=' ')

print('### while ###')
i = 0
while i <= 10:
    if i == 10:
        print(i)
    else:
        print(i, end=' ')
    i += 1

print('### for ###')
for i in range(10, -1, -1):
    if i == 0:
        print(i)
    else:
        print(i, end=' ')

print('### while ###')
i = 10
while i >= 0:
    if i == 0:
        print(i)
    else:
        print(i, end=' ')
    i -= 1

print('----------------')
for i in range(8):
    print('#' * i)

print('----------------')
for i in range(8):
    print('')
    for j in range(8):
        print('*', end=' ')
print()

print('----------------')
for i in range(11):
    print(str(i) + ' x ' + str(i) + ' = ' + str(i * i))

print('----------------')
lists = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for i in lists:
    print(i)

print('----------------')
for i in range(101):
    if i % 2 == 0:
        print(i, end=' ')
print()

print('----------------')
for i in range(101):
    if i % 2 == 1:
        print(i, end=' ')
print()

print('----------------')
total = 0
for i in range(101):
    total += i
print(total)

print('----------------')
evens = 0
odds = 0
for i in range(101):
    if i % 2 == 0:
        evens += i
    else:
        odds += i
print('evens', evens)
print('odds', odds)

print('----------------')
from data.countries import countries

for c in countries:
    if 'land' in c:
        print(c, end=',')
print()

print('----------------')
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruits = []
for i in range(len(fruits) - 1, -1, -1):
    print(i)
    new_fruits.append(fruits[i])
print(new_fruits)

print('----------------')
from data.countries_data import countries_data

total = []
for i in range(len(countries_data)):
    total += countries_data[i]['languages']
print(len(total))
count = pandas.value_counts(total)
print(count)
